import React from "react";
import clsx from "clsx";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import Heading from "@theme/Heading";

import styles from "./index.module.css";

function Hero() {
  return (
    <header className={clsx("hero", styles.heroBanner)}>
      <div className="container">
        <div className={styles.heroBadge}>Open Source · MIT</div>
        <Heading as="h1" className={styles.heroTitle}>
          Solviora Agent
        </Heading>
        <p className={styles.heroSubtitle}>
          Terminal-first AI agent for developers.
          One config, many providers, zero lock-in.
        </p>
        <div className={styles.heroButtons}>
          <Link className="button button--primary button--lg" to="/docs/quickstart">
            Get Started
          </Link>
          <Link className="button button--outline button--lg" to="/docs/cli-basics">
            Explore the CLI
          </Link>
        </div>
      </div>
    </header>
  );
}

interface FeatureItem {
  title: string;
  description: string;
  icon: string;
}

const features: FeatureItem[] = [
  {
    title: "Provider-agnostic",
    description:
      "Connect to OpenAI, Anthropic, Gemini, DeepSeek, Ollama, LM Studio, and more. Switch with a single config change.",
    icon: "↔",
  },
  {
    title: "Built-in tools",
    description:
      "Execute code, search the web, manage files, interact with databases — all from a curated toolbox you can extend.",
    icon: "⚡",
  },
  {
    title: "Terminal-native",
    description:
      "Runs where you work. Rich CLI, messaging gateway for Telegram and Discord, plus a full TUI experience.",
    icon: "▶",
  },
];

function Features() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {features.map((f, i) => (
            <div key={i} className="col col--4">
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
          Up and running in three commands
        </Heading>
        <div className="row">
          <div className="col col--6 col--offset-3">
            <div className={styles.codeBlock}>
              <code>
                <span className={styles.comment}># Install</span>
                <br />
                <span className={styles.command}>pip install solviora-agent</span>
                <br />
                <br />
                <span className={styles.comment}># Set your API key</span>
                <br />
                <span className={styles.command}>export OPENAI_API_KEY=sk-...</span>
                <br />
                <br />
                <span className={styles.comment}># Start chatting</span>
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
      title={`${siteConfig.title} — ${siteConfig.tagline}`}
      description="Solviora Agent: a terminal-first, provider-agnostic AI agent for developers. Connect to any LLM, use built-in tools, extend with plugins."
    >
      <Hero />
      <main>
        <Features />
        <QuickLook />
      </main>
    </Layout>
  );
}
