# Client Separation Strategy

## Critical Architectural Correction

Client projects must not live as permanent sub-sites inside a generic shared repository.

The following businesses are independent commercial entities:

- Deleite del Campo
- Catering Marbella
- Huertos Munay

Each one must evolve into its own standalone repository and deployment pipeline.

## Recommended Repository Structure

### Corporate Infrastructure

- nox-client-network
- nox-assets
- nox-automation
- nox-crm

### Independent Client Projects

- deleite-del-campo-site
- catering-marbella-site
- huertos-munay-site

## Why Separation Matters

Benefits:

- isolated branding
- cleaner deployments
- easier maintenance
- independent domains
- stronger SEO
- lower technical coupling
- client ownership flexibility

## Migration Plan

### Phase 1

Keep existing projects operational inside the current repository.

### Phase 2

Clone each client project into its own repository.

### Phase 3

Connect each repository to independent deployment infrastructure.

### Phase 4

Convert the current repository into a portfolio and orchestration hub instead of a multi-client host.
