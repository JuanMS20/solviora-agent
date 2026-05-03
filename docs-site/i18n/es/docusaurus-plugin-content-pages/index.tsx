import React from "react";
import clsx from "clsx";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import Link from "@docusaurus/Link";
import Heading from "@theme/Heading";
import styles from "./index.module.css";

function Hero() {
  return (
    <header className={clsx("hero", styles.heroBanner)}>
      <div className="container">
        <div className={styles.heroBadge}>Código abierto · MIT</div>
        <Heading as="h1" className={styles.heroTitle}>
          Solviora Agent
        </Heading>
        <p className={styles.heroSubtitle}>
          Agente de IA para terminal, diseñado para desarrolladores.
          Una configuración, muchos proveedores, sin dependencias.
        </p>
        <div className={styles.heroButtons}>
          <Link className="button button--primary button--lg" to="/docs/quickstart">
            Inicio rápido
          </Link>
          <Link className="button button--outline button--lg" to="/docs/cli-basics">
            Explorar la CLI
          </Link>
        </div>
      </div>
    </header>
  );
}

const features = [
  {
    title: "Agnóstico al proveedor",
    description:
      "Funciona con OpenAI, Anthropic, Google, Mistral, y más. Cambia de proveedor con un solo ajuste.",
    icon: "↔",
  },
  {
    title: "Herramientas integradas",
    description:
      "Lee y escribe archivos, ejecuta código, busca en la web y gestiona tu terminal — todo desde una conversación.",
    icon: "⚡",
  },
  {
    title: "Terminal nativo",
    description:
      "Interfaz interactiva en terminal con autocompletado, temas, sesiones y soporte completo de TUI.",
    icon: "▶",
  },
];

function Features() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {features.map((f, i) => (
            <div className="col col--4" key={i}>
              <div className={clsx("solviora-card", styles.featureCard)}>
                <div className={styles.featureIcon}>{f.icon}</div>
                <Heading as="h3">{f.title}</Heading>
                <p>{f.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function QuickLook() {
  return (
    <section className={styles.quickLook}>
      <div className="container">
        <Heading as="h2" className={styles.sectionTitle}>
          Empieza en segundos
        </Heading>
        <div className="row">
          <div className="col col--6 col--offset-3">
            <div className={styles.codeBlock}>
              <code>
                <span className={styles.comment}># Instalar</span>
                <br />
                <span className={styles.command}>pip install solviora-agent</span>
                <br />
                <br />
                <span className={styles.comment}># Configurar clave API</span>
                <br />
                <span className={styles.command}>export OPENAI_API_KEY=sk-...</span>
                <br />
                <br />
                <span className={styles.comment}># Iniciar</span>
                <br />
                <span className={styles.command}>solviora</span>
              </code>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home(): JSX.Element {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title} — Documentación`}
      description="Documentación oficial de Solviora Agent"
    >
      <Hero />
      <main>
        <Features />
        <QuickLook />
      </main>
    </Layout>
  );
}
