Requisitos Funcionais — Sistema Unificado de Conhecimento
## 1. Núcleo de Conhecimento

- ~~O sistema deve armazenar conhecimento em arquivos Markdown l~cai.~~

- ~~Deve permitir criação, edição e exclusão de notas sem dependência de banco.~~

- ~~Deve suportar links entre notas (bidirecionais).~~

- ~~Deve manter índices manuais editáveis pelo usuário.~~

- ~~Deve permitir anexar assets (imagens/diagramas) às notas por link.~~

## 2. Captura e Inbox

- ~~Deve existir uma Inbox para notas rápidas não classificadas.~~

- ~~O sistema deve permitir promoção manual de itens da Inbox para pastas finais.~~

- ~~Nenhuma classificação automática deve ser obrigatória.~~

## 3. Referências (Zotero)

O sistema deve ler metadados exportados do Zotero (BibTeX/JSON).

Deve permitir linkar notas a referências sem copiar PDFs.

PDFs não devem ser modificados nem versionados pelo sistema.

O sistema deve identificar novas referências desde a última sincronização.

## 4. Datasets

Deve suportar datasets em formato de arquivo (CSV, JSON, imagens, texto).

Deve separar claramente dados brutos, processados e derivados.

Dados brutos não devem ser alterados após ingestão.

Deve permitir reprocessar datasets a partir da versão bruta.

Deve registrar metadados dos datasets (origem, data, versão).

## 5. Banco de Dados Operacional

O sistema deve usar banco relacional apenas para dados estruturados.

Deve armazenar no banco:

metadados

estatísticas

embeddings

logs de execução

O banco não deve ser usado para armazenar conhecimento conceitual.

Deve ser possível gerar dump lógico completo do banco.

## 6. Orquestração (Pipelines)

O sistema deve permitir pipelines automatizados para tarefas recorrentes.

Cada pipeline deve ser idempotente (pode rodar mais de uma vez).

Pipelines devem ser composições de scripts independentes.

Deve ser possível executar scripts fora do orquestrador.

O sistema deve registrar status e falhas das execuções.

## 7. Geração Automática de Conteúdo

O sistema deve gerar textos sintéticos a partir de:

notas existentes

metadados de referências

datasets

Deve gerar imagens/visualizações a partir de datasets.

Conteúdo gerado deve ser salvo fora do núcleo de conhecimento.

O sistema não deve sobrescrever notas humanas automaticamente.

Deve permitir revisão humana antes da incorporação.

## 8. Versionamento

O sistema deve permitir versionar todo conteúdo gerado e curado.

Deve manter histórico de alterações das notas.

Deve permitir rollback para estados anteriores.

Versionamento não deve depender de serviços externos.

## 9. Backup

O sistema deve realizar backup apenas de dados gerados e curados.

PDFs e fontes originais devem ser excluídos do backup.

O backup deve ser:

incremental

criptografado

restaurável

Deve ser possível restaurar seletivamente partes do sistema.

Deve existir política de retenção configurável.