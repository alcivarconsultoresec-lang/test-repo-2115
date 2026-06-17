"""
Sistema Industrial de Gestión de Datos OSINT (Open Source Intelligence)

Este framework está diseñado para la recolección, procesamiento y gestión de datos
provenientes ÚNICAMENTE de fuentes públicas oficiales, APIs autorizadas y datasets
de acceso abierto que permiten su uso comercial y redistribución.

CARACTERÍSTICAS PRINCIPALES:
1. Arquitectura modular por fuentes de datos
2. Validación y limpieza de datos automatizada
3. Segmentación inteligente por nichos
4. Logging completo para auditoría y cumplimiento
5. Exportación a múltiples formatos (CSV, JSON, SQLite, Parquet)

FUENTES COMPATIBLES (Ejemplos):
- APIs gubernamentales abiertas (data.gov, EU Open Data Portal)
- Datasets de organizaciones internacionales (ONU, Banco Mundial, OMS)
- Repositorios académicos y científicos (arXiv, PubMed Central)
- Directorios empresariales con licencia abierta
- Datos meteorológicos, geográficos y estadísticos públicos

NOTA LEGAL: Este sistema NO realiza web scraping. Todas las recolecciones
deben hacerse mediante APIs oficiales o descargas directas de datasets
que explícitamente permitan su uso bajo licencias como CC-BY, ODbL, o dominio público.
"""

import pandas as pd
import requests
import json
import sqlite3
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, ValidationError
import hashlib
import time
import logging

# Configuración del logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/osint_system.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class DataSourceConfig(BaseModel):
    """Configuración para una fuente de datos"""
    name: str
    type: str  # 'api', 'csv_url', 'json_url', 'local_file'
    url: Optional[str] = None
    local_path: Optional[str] = None
    api_key_env: Optional[str] = None
    update_frequency: str  # 'daily', 'weekly', 'monthly'
    license_type: str  # 'CC-BY', 'ODbL', 'Public Domain', etc.
    rate_limit: int = 10  # requests per second
    fields_mapping: Dict[str, str]  # Mapeo de campos originales a estandarizados


class DataRecord(BaseModel):
    """Esquema base para registros depurados"""
    id: str
    source: str
    collection_date: str
    niche_category: str
    data: Dict[str, Any]
    quality_score: float
    verification_status: str  # 'verified', 'pending', 'flagged'


class IndustrialOSINTSystem:
    """Sistema principal de gestión de datos OSINT"""
    
    def __init__(self, db_path: str = "data/osint_database.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.sources: Dict[str, DataSourceConfig] = {}
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Industrial-OSINT-System/1.0 (Educational/Research Use)'
        })
        
        logger.info("Sistema OSINT inicializado correctamente")
        self._initialize_database()
    
    def _initialize_database(self):
        """Inicializa la base de datos SQLite con las tablas necesarias"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Tabla de fuentes registradas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS data_sources (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                license_type TEXT NOT NULL,
                last_update TIMESTAMP,
                record_count INTEGER DEFAULT 0
            )
        ''')
        
        # Tabla principal de registros
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id TEXT PRIMARY KEY,
                source_id TEXT NOT NULL,
                niche_category TEXT NOT NULL,
                collection_date TIMESTAMP NOT NULL,
                quality_score REAL NOT NULL,
                verification_status TEXT NOT NULL,
                raw_data JSON NOT NULL,
                FOREIGN KEY (source_id) REFERENCES data_sources(id)
            )
        ''')
        
        # Índices para optimizar consultas
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_niche ON records(niche_category)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_source ON records(source_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_quality ON records(quality_score)')
        
        conn.commit()
        conn.close()
        logger.info(f"Base de datos inicializada en {self.db_path}")
    
    def register_source(self, config: DataSourceConfig):
        """Registra una nueva fuente de datos compatible"""
        if config.name in self.sources:
            logger.warning(f"La fuente {config.name} ya está registrada")
            return
        
        # Validar que la configuración sea correcta
        try:
            DataSourceConfig(**config.dict())
            self.sources[config.name] = config
            
            # Registrar en la base de datos
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO data_sources 
                (id, name, type, license_type, last_update, record_count)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (config.name, config.name, config.type, config.license_type, None, 0))
            conn.commit()
            conn.close()
            
            logger.info(f"Fuente registrada exitosamente: {config.name} ({config.license_type})")
        except ValidationError as e:
            logger.error(f"Error al validar configuración de fuente: {e}")
            raise
    
    def _fetch_from_api(self, config: DataSourceConfig) -> List[Dict]:
        """Obtiene datos desde una API oficial (implementación genérica)"""
        if not config.url:
            raise ValueError(f"URL no definida para la fuente {config.name}")
        
        headers = self.session.headers.copy()
        if config.api_key_env:
            import os
            api_key = os.getenv(config.api_key_env)
            if api_key:
                headers['Authorization'] = f"Bearer {api_key}"
        
        all_data = []
        page = 1
        
        while True:
            try:
                # Ejemplo de paginación estándar (ajustar según la API específica)
                params = {'page': page, 'per_page': 100}
                response = self.session.get(config.url, headers=headers, params=params, timeout=30)
                response.raise_for_status()
                
                data = response.json()
                
                if isinstance(data, list):
                    all_data.extend(data)
                    if len(data) < 100:  # No hay más datos
                        break
                elif isinstance(data, dict) and 'data' in data:
                    all_data.extend(data['data'])
                    if len(data['data']) < 100:
                        break
                else:
                    logger.warning(f"Formato de respuesta no esperado para {config.name}")
                    break
                
                page += 1
                time.sleep(1 / config.rate_limit)  # Respetar rate limit
                
            except requests.exceptions.RequestException as e:
                logger.error(f"Error al obtener datos de {config.name}: {e}")
                break
        
        return all_data
    
    def _fetch_from_url(self, config: DataSourceConfig) -> pd.DataFrame:
        """Descarga datos desde URLs de CSV o JSON públicos"""
        if not config.url:
            raise ValueError(f"URL no definida para la fuente {config.name}")
        
        try:
            if config.type == 'csv_url':
                return pd.read_csv(config.url)
            elif config.type == 'json_url':
                response = self.session.get(config.url, timeout=30)
                response.raise_for_status()
                return pd.DataFrame(response.json())
            else:
                raise ValueError(f"Tipo de URL no soportado: {config.type}")
        except Exception as e:
            logger.error(f"Error al descargar desde {config.url}: {e}")
            return pd.DataFrame()
    
    def _fetch_from_local(self, config: DataSourceConfig) -> pd.DataFrame:
        """Carga datos desde archivos locales"""
        if not config.local_path:
            raise ValueError(f"Ruta local no definida para la fuente {config.name}")
        
        path = Path(config.local_path)
        if not path.exists():
            logger.error(f"Archivo no encontrado: {path}")
            return pd.DataFrame()
        
        try:
            if path.suffix == '.csv':
                return pd.read_csv(path)
            elif path.suffix == '.json':
                return pd.read_json(path)
            elif path.suffix in ['.parquet', '.pq']:
                return pd.read_parquet(path)
            else:
                logger.warning(f"Formato de archivo no soportado: {path.suffix}")
                return pd.DataFrame()
        except Exception as e:
            logger.error(f"Error al leer archivo local {path}: {e}")
            return pd.DataFrame()
    
    def _generate_record_id(self, source: str, data: Dict) -> str:
        """Genera un ID único para cada registro"""
        content = f"{source}:{json.dumps(data, sort_keys=True)}"
        return hashlib.sha256(content.encode()).hexdigest()[:32]
    
    def _calculate_quality_score(self, record: Dict, config: DataSourceConfig) -> float:
        """Calcula un score de calidad basado en completitud y consistencia"""
        score = 0.0
        max_score = 0.0
        
        for original_field, standardized_field in config.fields_mapping.items():
            max_score += 1.0
            if original_field in record and record[original_field]:
                value = record[original_field]
                # Verificar que el valor no esté vacío o sea nulo
                if isinstance(value, str) and value.strip():
                    score += 1.0
                elif not isinstance(value, str) and value is not None:
                    score += 1.0
        
        return round(score / max_score, 2) if max_score > 0 else 0.0
    
    def _categorize_niche(self, record: Dict, config: DataSourceConfig) -> str:
        """Clasifica automáticamente el registro en un nicho"""
        # Implementación básica - personalizable según el tipo de dato
        # En producción, esto usaría ML o reglas específicas por industria
        
        text_content = " ".join([
            str(record.get(field, "")) 
            for field in config.fields_mapping.keys() 
            if field in record
        ]).lower()
        
        # Reglas simples de categorización (ejemplo)
        niche_keywords = {
            'healthcare': ['hospital', 'medical', 'health', 'clinic', 'pharma'],
            'technology': ['software', 'tech', 'digital', 'ai', 'cloud'],
            'finance': ['bank', 'financial', 'investment', 'insurance', 'fintech'],
            'education': ['university', 'school', 'education', 'academic', 'research'],
            'government': ['government', 'public', 'administration', 'municipal'],
            'retail': ['store', 'retail', 'shop', 'commerce', 'market'],
            'manufacturing': ['manufacturing', 'factory', 'production', 'industrial'],
            'energy': ['energy', 'renewable', 'oil', 'gas', 'power'],
        }
        
        for niche, keywords in niche_keywords.items():
            if any(keyword in text_content for keyword in keywords):
                return niche
        
        return 'general'  # Categoría por defecto
    
    def process_source(self, source_name: str) -> int:
        """Procesa todos los datos de una fuente registrada"""
        if source_name not in self.sources:
            logger.error(f"Fuente {source_name} no registrada")
            return 0
        
        config = self.sources[source_name]
        logger.info(f"Iniciando procesamiento de fuente: {source_name}")
        
        # Obtener datos según el tipo de fuente
        if config.type == 'api':
            raw_data = self._fetch_from_api(config)
            df = pd.DataFrame(raw_data)
        elif config.type in ['csv_url', 'json_url']:
            df = self._fetch_from_url(config)
        elif config.type == 'local_file':
            df = self._fetch_from_local(config)
        else:
            logger.error(f"Tipo de fuente no soportado: {config.type}")
            return 0
        
        if df.empty:
            logger.warning(f"No se obtuvieron datos de {source_name}")
            return 0
        
        # Procesar cada registro
        processed_count = 0
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        for _, row in df.iterrows():
            try:
                record_dict = row.to_dict()
                
                # Generar ID único
                record_id = self._generate_record_id(source_name, record_dict)
                
                # Calcular score de calidad
                quality_score = self._calculate_quality_score(record_dict, config)
                
                # Solo procesar registros con calidad mínima aceptable
                if quality_score < 0.5:
                    continue
                
                # Categorizar nicho
                niche = self._categorize_niche(record_dict, config)
                
                # Estandarizar campos según mapping
                standardized_data = {}
                for original_field, standardized_field in config.fields_mapping.items():
                    if original_field in record_dict:
                        standardized_data[standardized_field] = record_dict[original_field]
                
                # Crear objeto DataRecord
                data_record = {
                    'id': record_id,
                    'source': source_name,
                    'collection_date': datetime.now().isoformat(),
                    'niche_category': niche,
                    'data': standardized_data,
                    'quality_score': quality_score,
                    'verification_status': 'pending' if quality_score < 0.8 else 'verified'
                }
                
                # Insertar en base de datos
                cursor.execute('''
                    INSERT OR REPLACE INTO records 
                    (id, source_id, niche_category, collection_date, quality_score, 
                     verification_status, raw_data)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    record_id, source_name, niche, 
                    data_record['collection_date'], quality_score,
                    data_record['verification_status'],
                    json.dumps(standardized_data)
                ))
                
                processed_count += 1
                
            except Exception as e:
                logger.error(f"Error al procesar registro: {e}")
                continue
        
        # Actualizar metadatos de la fuente
        cursor.execute('''
            UPDATE data_sources 
            SET last_update = ?, record_count = ?
            WHERE id = ?
        ''', (datetime.now().isoformat(), processed_count, source_name))
        
        conn.commit()
        conn.close()
        
        logger.info(f"Procesamiento completado: {processed_count} registros de {source_name}")
        return processed_count
    
    def query_by_niche(self, niche: str, min_quality: float = 0.7, limit: int = 1000) -> pd.DataFrame:
        """Consulta registros por nicho con filtro de calidad"""
        conn = sqlite3.connect(self.db_path)
        
        query = '''
            SELECT id, source_id, niche_category, collection_date, 
                   quality_score, verification_status, raw_data
            FROM records
            WHERE niche_category = ? AND quality_score >= ?
            ORDER BY quality_score DESC, collection_date DESC
            LIMIT ?
        '''
        
        df = pd.read_sql_query(query, conn, params=(niche, min_quality, limit))
        conn.close()
        
        # Parsear JSON de raw_data
        if not df.empty:
            df['structured_data'] = df['raw_data'].apply(json.loads)
        
        return df
    
    def get_segmented_databases(self, output_dir: str = "output/segmented"):
        """Exporta bases de datos segmentadas por nicho"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Obtener lista de nichos
        cursor.execute('SELECT DISTINCT niche_category FROM records')
        niches = [row[0] for row in cursor.fetchall()]
        
        exported_files = []
        
        for niche in niches:
            # Exportar a CSV
            csv_path = output_path / f"{niche}_database.csv"
            query = '''
                SELECT id, source_id, collection_date, quality_score, 
                       verification_status, raw_data
                FROM records
                WHERE niche_category = ?
                ORDER BY quality_score DESC
            '''
            df = pd.read_sql_query(query, conn, params=(niche,))
            df.to_csv(csv_path, index=False)
            exported_files.append(str(csv_path))
            
            # Exportar a Parquet (mejor rendimiento para grandes volúmenes)
            parquet_path = output_path / f"{niche}_database.parquet"
            df.to_parquet(parquet_path, index=False)
            exported_files.append(str(parquet_path))
            
            logger.info(f"Base de datos exportada para nicho '{niche}': {len(df)} registros")
        
        conn.close()
        
        # Exportar base de datos completa consolidada
        full_db_path = output_path / "consolidated_database.parquet"
        full_df = pd.read_sql_query('SELECT * FROM records', conn)
        full_df.to_parquet(full_db_path, index=False)
        exported_files.append(str(full_db_path))
        
        logger.info(f"Exportación completada: {len(exported_files)} archivos generados")
        return exported_files
    
    def get_statistics(self) -> Dict[str, Any]:
        """Obtiene estadísticas generales del sistema"""
        conn = sqlite3.connect(self.db_path)
        
        stats = {}
        
        # Total de registros
        stats['total_records'] = pd.read_sql_query(
            'SELECT COUNT(*) as count FROM records', conn
        )['count'].iloc[0]
        
        # Registros por nicho
        stats['by_niche'] = pd.read_sql_query('''
            SELECT niche_category, COUNT(*) as count, AVG(quality_score) as avg_quality
            FROM records
            GROUP BY niche_category
            ORDER BY count DESC
        ''', conn).to_dict('records')
        
        # Registros por fuente
        stats['by_source'] = pd.read_sql_query('''
            SELECT source_id, COUNT(*) as count, AVG(quality_score) as avg_quality
            FROM records
            GROUP BY source_id
            ORDER BY count DESC
        ''', conn).to_dict('records')
        
        # Distribución de calidad (corregido para SQLite)
        quality_query = '''
            SELECT 
                CASE 
                    WHEN quality_score >= 0.9 THEN 'excellent'
                    WHEN quality_score >= 0.7 THEN 'good'
                    WHEN quality_score >= 0.5 THEN 'acceptable'
                    ELSE 'low'
                END as quality_level,
                COUNT(*) as count
            FROM records
            GROUP BY quality_level
        '''
        stats['quality_distribution'] = pd.read_sql_query(quality_query, conn).to_dict('records')
        
        conn.close()
        
        return stats


# Ejemplo de uso y configuración de fuentes legítimas
if __name__ == "__main__":
    # Inicializar el sistema
    system = IndustrialOSINTSystem()
    
    # EJEMPLO 1: Datos gubernamentales de EE.UU. (data.gov)
    # Nota: Esta es una configuración de ejemplo. Debes verificar la API específica.
    us_gov_source = DataSourceConfig(
        name="us_business_registry",
        type="api",
        url="https://api.example.gov/businesses",  # URL ficticia - usar API real
        api_key_env="US_GOV_API_KEY",
        update_frequency="weekly",
        license_type="Public Domain",
        rate_limit=5,
        fields_mapping={
            "business_id": "id",
            "company_name": "name",
            "industry_code": "industry",
            "registration_date": "created_date",
            "status": "status",
            "address": "location"
        }
    )
    
    # EJEMPLO 2: Dataset europeo de empresas (EU Open Data Portal)
    eu_companies_source = DataSourceConfig(
        name="eu_companies_dataset",
        type="csv_url",
        url="https://data.europa.eu/euodp/data/dataset/example-companies.csv",  # URL ficticia
        update_frequency="monthly",
        license_type="CC-BY-4.0",
        rate_limit=10,
        fields_mapping={
            "CompanyID": "id",
            "CompanyName": "name",
            "Sector": "industry",
            "Country": "country",
            "Employees": "size",
            "Website": "web_url"
        }
    )
    
    # EJEMPLO 3: Datos del Banco Mundial
    world_bank_source = DataSourceConfig(
        name="world_bank_indicators",
        type="api",
        url="https://api.worldbank.org/v2/countries/all/indicators",  # URL real
        update_frequency="monthly",
        license_type="CC-BY-4.0",
        rate_limit=3,
        fields_mapping={
            "indicator.id": "indicator_code",
            "indicator.value": "indicator_name",
            "country.id": "country_code",
            "country.value": "country_name",
            "date": "year",
            "value": "value"
        }
    )
    
    # Registrar fuentes (descomentar las que quieras usar con URLs reales)
    # system.register_source(us_gov_source)
    # system.register_source(eu_companies_source)
    # system.register_source(world_bank_source)
    
    # Procesar una fuente específica
    # records_processed = system.process_source("world_bank_indicators")
    
    # Consultar datos por nicho
    # tech_companies = system.query_by_niche("technology", min_quality=0.7)
    # print(f"Empresas tecnológicas encontradas: {len(tech_companies)}")
    
    # Exportar bases de datos segmentadas
    # exported_files = system.get_segmented_databases()
    
    # Obtener estadísticas
    stats = system.get_statistics()
    print("\n=== ESTADÍSTICAS DEL SISTEMA ===")
    print(f"Total de registros: {stats['total_records']}")
    print("\nRegistros por nicho:")
    for niche_data in stats['by_niche']:
        print(f"  - {niche_data['niche_category']}: {niche_data['count']} registros "
              f"(calidad promedio: {niche_data['avg_quality']:.2f})")
    
    print("\n" + "="*50)
    print("Sistema listo para usar.")
    print("IMPORTANTE: Configura fuentes reales con APIs oficiales antes de ejecutar.")
    print("="*50)
