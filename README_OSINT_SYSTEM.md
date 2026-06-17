# Sistema Industrial OSINT - Guía de Uso

## Descripción

Este sistema es un framework profesional para la gestión de datos OSINT (Open Source Intelligence) que opera **exclusivamente** con fuentes legítimas y autorizadas.

## Características Principales

### ✅ Lo que SÍ hace:
- Conecta con APIs gubernamentales oficiales (data.gov, EU Open Data, etc.)
- Procesa datasets públicos con licencias abiertas (CC-BY, ODbL, Dominio Público)
- Limpia y depura datos automáticamente
- Segmenta por nichos de industria usando clasificación inteligente
- Calcula scores de calidad para cada registro
- Exporta a múltiples formatos (CSV, Parquet, SQLite, JSON)
- Mantiene logs completos para auditoría
- Respeta rate limits y términos de servicio

### ❌ Lo que NO hace:
- NO realiza web scraping de sitios web
- NO bypassea protecciones o CAPTCHAs
- NO accede a datos privados o protegidos
- NO viola términos de servicio de ninguna plataforma

## Fuentes de Datos Recomendadas

### Gubernamentales
- **USA**: data.gov, census.gov, sec.gov/edgar
- **UE**: data.europa.eu, EU Open Data Portal
- **Internacional**: data.un.org, worldbank.org, imf.org

### Organizaciones Internacionales
- Banco Mundial: api.worldbank.org
- ONU: data.un.org
- OMS: WHO Open Data
- OCDE: stats.oecd.org

### Científicas/Académicas
- arXiv.org (papers científicos)
- PubMed Central (salud)
- Kaggle Datasets (diversos temas con licencia)
- Google Dataset Search

### Empresariales (con licencia abierta)
- OpenCorporates (datos corporativos básicos)
- Crunchbase (versión API gratuita limitada)
- Registros mercantiles oficiales de cada país

## Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt

# Crear variables de entorno (opcional, para APIs que requieren key)
cp .env.example .env
# Editar .env con tus API keys
```

## Uso Básico

```python
from industrial_osint_system import IndustrialOSINTSystem, DataSourceConfig

# Inicializar el sistema
system = IndustrialOSINTSystem()

# Configurar una fuente de datos (ejemplo: Banco Mundial)
world_bank = DataSourceConfig(
    name="world_bank_data",
    type="api",
    url="https://api.worldbank.org/v2/countries/all/indicators",
    update_frequency="monthly",
    license_type="CC-BY-4.0",
    rate_limit=3,
    fields_mapping={
        "indicator.id": "indicator_code",
        "value": "value",
        "country.value": "country_name"
    }
)

# Registrar la fuente
system.register_source(world_bank)

# Procesar datos
records = system.process_source("world_bank_data")

# Consultar por nicho
tech_data = system.query_by_niche("technology", min_quality=0.7)

# Exportar bases segmentadas
files = system.get_segmented_databases()

# Ver estadísticas
stats = system.get_statistics()
```

## Estructura del Sistema

```
industrial_osint_system.py  # Código principal
requirements.txt            # Dependencias
data/                       # Base de datos SQLite
logs/                       # Logs de auditoría
output/segmented/          # Bases exportadas por nicho
```

## Nichos Disponibles

El sistema clasifica automáticamente en:
- Healthcare (salud)
- Technology (tecnología)
- Finance (finanzas)
- Education (educación)
- Government (gobierno)
- Retail (comercio)
- Manufacturing (manufactura)
- Energy (energía)
- General (otros)

## Calidad de Datos

Cada registro recibe un score (0.0 - 1.0) basado en:
- Completitud de campos
- Consistencia de datos
- Validación de formatos
- Fuente verificada

Solo se procesan registros con score ≥ 0.5

## Consideraciones Legales

### Licencias Compatibles
- ✅ CC-BY (Creative Commons Attribution)
- ✅ CC0 (Dominio Público)
- ✅ ODbL (Open Database License)
- ✅ Datos gubernamentales de dominio público
- ✅ APIs con términos explícitos de uso comercial

### Buenas Prácticas
1. Siempre verifica la licencia de cada dataset
2. Atribuye correctamente las fuentes
3. Respeta los rate limits de las APIs
4. No redistribuyas datos con restricciones
5. Mantén logs de procedencia de datos

## Escalabilidad

Para producción a gran escala:
- Usar PostgreSQL en lugar de SQLite
- Implementar colas de procesamiento (Celery/RQ)
- Configurar actualizaciones automáticas programadas
- Usar almacenamiento en la nube para exports
- Implementar caché para respuestas de APIs

## Soporte y Extensiones

Para añadir nuevas fuentes:
1. Identificar API oficial o dataset público
2. Verificar licencia de uso
3. Configurar DataSourceConfig con mapeo de campos
4. Registrar en el sistema
5. Ejecutar procesamiento

## Ejemplos de Configuración

Ver el archivo `industrial_osint_system.py` para ejemplos completos de configuración de fuentes reales.

---

**Nota**: Este sistema es una herramienta educativa y profesional para gestión ética de datos públicos. El usuario es responsable de verificar el cumplimiento legal en su jurisdicción.
