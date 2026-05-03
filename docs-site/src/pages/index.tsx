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
          aria-label="Copy command"
        >
          {copied ? "Copied ✓" : "Copy"}
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
            <p className={styles.heroLabel}>Documentation</p>
            <Heading as="h1" className={styles.heroTitle}>
              Docs for Solviora Agent
            </Heading>
            <p className={styles.heroBody}>
              Solviora is a CLI-first agent for automation, tools, and messaging
              workflows. Start with installation, connect a provider, and run
              your first session in a few minutes.
            </p>
            <div className={styles.heroLinks}>
              <Link to="/docs/quickstart">Quickstart&nbsp;→</Link>
              <Link to="/docs/installation">Installation</Link>
              <Link to="/docs/configuration">Configuration</Link>
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
    heading: "Start here",
    links: [
      {
        label: "Quickstart",
        href: "/docs/quickstart",
        description: "Install, configure, and run your first session.",
      },
      {
        label: "Install on Windows / macOS / Linux",
        href: "/docs/installation",
        description: "One-line installer, pip, and platform-specific notes.",
      },
      {
        label: "Configure API keys",
        href: "/docs/configuration",
        description: "Set up your .env and config.yaml.",
      },
    ],
  },
  {
    heading: "Go deeper",
    links: [
      {
        label: "Choose a model provider",
        href: "/docs/providers",
        description: "OpenAI, Anthropic, Gemini, Ollama, LM Studio, and more.",
      },
      {
        label: "Skills overview",
        href: "/docs/skills",
        description: "On-demand knowledge documents and SKILL.md format.",
      },
      {
        label: "Gateway setup",
        href: "/docs/messaging",
        description: "Telegram, Discord, Slack, WhatsApp, and more platforms.",
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

/* ── Why Solviora ──────────────────────────────────────── */

const pillars = [
  {
    verb: "Solves",
    description:
      "Resolves complex tasks and automates workflows with a rich built-in toolset.",
  },
  {
    verb: "Remembers",
    description:
      "Keeps persistent memory of preferences, projects, and context across sessions.",
  },
  {
    verb: "Evolves",
    description:
      "Learns from interactions and turns repetitive processes into reusable skills.",
  },
];

function WhySolviora() {
  return (
    <section className={styles.whySection}>
      <div className="container">
        <Heading as="h2" className={styles.whyHeading}>
          Why "Solviora"?
        </Heading>
        <p className={styles.whyBody}>
          "Solviora" captures the core idea of the product: an agent that
          solves&nbsp;tasks, remembers context across sessions, and evolves with
          use. The name summarizes the value proposition&nbsp;— persistent
          memory, reusable skills, extensible tools, and a self-hosted approach
          with no vendor lock-in.
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
          <strong>Solviora</strong> — The agent that solves, remembers, and
          evolves.
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
      title={`${siteConfig.title} — Docs`}
      description="Solviora Agent documentation. Install, configure providers, and run your first session."
    >
      <main>
        <QuickStart />
        <TaskNav />
        <WhySolviora />
      </main>
    </Layout>
  );
}
