# Solviora Agent

**Agente de IA nativo de terminal que hace el trabajo real.**

Busca en la web, escribe y ejecuta código, lee y escribe archivos, investiga, automatiza — y entrega resultados. Todo desde tu terminal, sin necesidad de navegador.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://python.org)
[![Docs](https://img.shields.io/badge/docs-solviora.dev-2BA8A0)](https://docs.solviora.dev)
[![Website](https://img.shields.io/badge/sitio-solviora.dev-8B5CF6)](https://solvioraagent.netlify.app)

> **Atribución:** Solviora Agent está construido sobre [Hermes Agent](https://github.com/NousResearch/hermes-agent) de [Nous Research](https://nousresearch.com), usado bajo la [Licencia MIT](LICENSE).

---

## Inicio rápido

### Instalación en un solo paso (recomendada)

Funciona en Linux, macOS y WSL2:

```bash
curl -fsSL https://raw.githubusercontent.com/JuanMS20/solviora-agent/main/scripts/install.sh | bash
source ~/.bashrc
solviora setup
solviora
```

### Instalar desde fuente

```bash
git clone https://github.com/JuanMS20/solviora-agent.git
cd solviora-agent
./setup-solviora.sh
```

Configura tu proveedor y empieza:

```bash
solviora setup          # Configuración en 3 pasos: proveedor → modelo → ¡listo!
solviora
```

Tu primer resultado en minutos. Sin navegador, sin IDE, sin fricción.

## Qué hace

- **Investigación web** — busca, extrae y resume cualquier tema
- **Código** — escribe, ejecuta y depura en cualquier lenguaje
- **Archivos** — lee, escribe, parchea y busca en tu proyecto
- **Memoria** — memoria persistente entre sesiones
- **Automatización** — delega subtareas, programa cron jobs
- **Skills** — instala paquetes de habilidades especializadas para tu flujo de trabajo

## Conectarse remotamente (opcional)

Solviora funciona completamente en tu terminal. Si necesitas acceso remoto:

```bash
solviora setup gateway  # Conecta Telegram, webhook o servidor API
```

Las pasarelas son extensiones opcionales — no se requieren para ninguna función principal.

## Comandos CLI

```
solviora "tu tarea"     # Ejecuta una tarea directamente
solviora                 # Sesión CLI interactiva
solviora model           # Elige proveedor LLM y modelo
solviora tools           # Configura herramientas habilitadas
solviora setup           # Ejecuta el asistente de configuración
solviora setup gateway   # Configura acceso remoto
solviora status          # Muestra el estado del sistema
solviora doctor          # Diagnostica problemas
```

## Configuración

- Archivo de configuración: `~/.solviora/config.yaml`
- Claves API: `~/.solviora/.env`
- Sesiones: `~/.solviora/sessions/`
- Skills: `~/.solviora/skills/`

## Documentación

Visita [docs.solviora.dev](https://docs.solviora.dev) para la documentación completa:

- [Inicio rápido](https://docs.solviora.dev/docs/quickstart)
- [Guía de instalación](https://docs.solviora.dev/docs/installation)
- [Referencia CLI](https://docs.solviora.dev/docs/cli-commands)
- [Proveedores](https://docs.solviora.dev/docs/providers)

### Ejecutar docs localmente

```bash
cd docs-site
npm install
npm run start
```

## Contribuir

¡Las contribuciones son bienvenidas! Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para las pautas.

## Licencia

MIT — consulta [LICENSE](LICENSE).

Este proyecto incluye código desarrollado originalmente por Nous Research (Hermes Agent), también bajo la Licencia MIT. Consulta [NOTICE](NOTICE) para más detalles.

