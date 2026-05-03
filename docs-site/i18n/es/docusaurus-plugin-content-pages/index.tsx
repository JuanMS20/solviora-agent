import React, { useState, useCallback } from "react";
import clsx from "clsx";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import Heading from "@theme/Heading";
import styles from "./index.module.css";

/* ── Install snippet data ─────────────────────────────── */

const installOptions = [
  {
    id: "curl",
    label: "curl",
    command: `curl -fsSL https://raw.githubusercontent.com/JuanMS20/solviora-agent/main/scripts/install.sh | bash\nsolviora setup && solviora`,
  },
  {
    id: "pip",
    label: "pip",
    command: `pip install solviora-agent\nsolviora setup && solviora`,
  },
];

/* ── Quick-start hero ─────────────────────────────────── */

function InstallBlock() {
  const [activeTab, setActiveTab] = useState("curl");
  const [copied, setCopied] = useState(false);

  const handleCopy = useCallback(() => {
    const option = installOptions.find((o) => o.id === activeTab);
    if (!option) return;
    navigator.clipboard.writeText(option.command).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    });
  }, [activeTab]);

  const current = installOptions.find((o) => o.id === activeTab)!;

  return (
    <div className={styles.installPanel}>
      <div className={styles.installHeader}>
        <div className={styles.installTabs}>
          {installOptions.map((opt) => (
            <button
              key={opt.id}
              className={clsx(
                styles.installTab,
                activeTab === opt.id && styles.installTabActive,
              )}
              onClick={() => { setActiveTab(opt.id); setCopied(false); }}
            >
              {opt.label}
            </button>
          ))}
        </div>
        <button
          className={clsx(styles.copyBtn, copied && styles.copyBtnCopied)}
          onClick={handleCopy}
          aria-label="Copiar comando"
        >
          {copied ? "Copiado ✓" : "Copiar"}
        </button>
      </div>
      <div className={styles.installCodeWrap}>
        <code>
          {current.command.split("\n").map((line, i, arr) => (
            <React.Fragment key={i}>
              {line.startsWith("#") ? (
                <span className={styles.comment}>{line}</span>
              ) : (
                <span className={styles.command}>{line}</span>
              )}
              {i < arr.length - 1 && <br />}
            </React.Fragment>
          ))}
        </code>
      </div>
    </div>
  );
}

function QuickStart() {
  return (
    <section className={styles.heroSection}>
      <div className="container">
        <div className="row">
          <div className="col col--7">
            <p className={styles.heroLabel}>Documentación</p>
            <Heading as="h1" className={styles.heroTitle}>
              Documentación de Solviora Agent
            </Heading>
            <p className={styles.heroBody}>
              Solviora es un agente orientado a CLI para automatización, tools y
              flujos de mensajería. Empieza por la instalación, conecta un
              provider y ejecuta tu primera sesión en pocos minutos.
            </p>
            <div className={styles.heroLinks}>
              <Link to="/docs/quickstart">Inicio rápido&nbsp;→</Link>
              <Link to="/docs/installation">Instalación</Link>
              <Link to="/docs/configuration">Configuración</Link>
              <Link to="/docs/providers">Providers</Link>
            </div>
          </div>
          <div className={clsx("col col--5", styles.codeColumn)}>
            <InstallBlock />
          </div>
        </div>
      </div>
    </section>
  );
}

/* ── Task-oriented navigation ──────────────────────────── */

interface TaskLink {
  label: string;
  href: string;
  description: string;
}

const taskGroups: { heading: string; links: TaskLink[] }[] = [
  {
    heading: "Empieza aquí",
    links: [
      {
        label: "Inicio rápido",
        href: "/docs/quickstart",
        description: "Instala, configura y ejecuta tu primera sesión.",
      },
      {
        label: "Instalar en Windows / macOS / Linux",
        href: "/docs/installation",
        description: "Instalador de una línea, pip y notas específicas por plataforma.",
      },
      {
        label: "Configurar claves API",
        href: "/docs/configuration",
        description: "Configura tu .env y config.yaml.",
      },
    ],
  },
  {
    heading: "Profundiza",
    links: [
      {
        label: "Elegir un proveedor de modelo",
        href: "/docs/providers",
        description: "OpenAI, Anthropic, Gemini, Ollama, LM Studio y más.",
      },
      {
        label: "Skills",
        href: "/docs/skills",
        description: "Documentos de conocimiento bajo demanda y formato SKILL.md.",
      },
      {
        label: "Configurar mensajería",
        href: "/docs/messaging",
        description: "Telegram, Discord, Slack, WhatsApp y más plataformas.",
      },
    ],
  },
];

function TaskNav() {
  return (
    <section className={styles.taskSection}>
      <div className="container">
        <div className="row">
          {taskGroups.map((group) => (
            <div key={group.heading} className="col col--6">
              <Heading as="h2" className={styles.taskHeading}>
                {group.heading}
              </Heading>
              <ul className={styles.taskList}>
                {group.links.map((link) => (
                  <li key={link.href} className={styles.taskItem}>
                    <Link to={link.href} className={styles.taskLink}>
                      {link.label}
                    </Link>
                    <p className={styles.taskDesc}>{link.description}</p>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ── ¿Por qué "Solviora"? ─────────────────────────────── */

const pillars = [
  {
    verb: "Solves",
    description:
      "Resuelve tareas complejas y automatiza flujos de trabajo.",
  },
  {
    verb: "Remembers",
    description:
      "Mantiene memoria persistente de preferencias, proyectos y contexto.",
  },
  {
    verb: "Evolves",
    description:
      "Aprende de interacciones y convierte procesos repetidos en skills reutilizables.",
  },
];

function WhySolviora() {
  return (
    <section className={styles.whySection}>
      <div className="container">
        <Heading as="h2" className={styles.whyHeading}>
          ¿Por qué "Solviora"?
        </Heading>
        <p className={styles.whyBody}>
          "Solviora" expresa la idea central del producto: un agente que
          resuelve tareas, recuerda contexto entre sesiones y evoluciona con el
          uso. El nombre resume la propuesta de valor&nbsp;— memoria
          persistente, skills reutilizables, tools extensibles y un enfoque
          self-hosted sin vendor lock-in.
        </p>
        <div className="row">
          {pillars.map((p) => (
            <div key={p.verb} className="col col--4">
              <div className={styles.pillarCard}>
                <strong className={styles.pillarVerb}>{p.verb}</strong>
                <p className={styles.pillarDesc}>{p.description}</p>
              </div>
            </div>
          ))}
        </div>
        <p className={styles.whyTagline}>
          <strong>Solviora</strong> — El agente que resuelve, recuerda y
          evoluciona.
        </p>
      </div>
    </section>
  );
}

/* ── Page ──────────────────────────────────────────────── */

export default function Home(): JSX.Element {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title} — Documentación`}
      description="Documentación oficial de Solviora Agent"
    >
      <main>
        <QuickStart />
        <TaskNav />
        <WhySolviora />
      </main>
    </Layout>
  );
}
