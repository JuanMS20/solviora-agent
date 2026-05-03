import type { SidebarsConfig } from "@docusaurus/plugin-content-docs";

const sidebars: SidebarsConfig = {
  docsSidebar: [
    {
      type: "doc",
      id: "index",
      label: "Docs Home",
    },
    {
      type: "category",
      label: "Getting Started",
      collapsed: false,
      items: ["installation", "quickstart", "learning-path"],
    },
    {
      type: "category",
      label: "User Guide",
      collapsed: false,
      items: [
        "cli-basics",
        "tui",
        "configuration",
        "providers",
        "messaging",
        "sessions",
        "security",
      ],
    },
    {
      type: "category",
      label: "Features",
      collapsed: false,
      items: [
        "tools",
        "features-memory",
        "skills",
        "features-skills",
        "features-mcp",
        "features-voice",
        "features-personality",
        "features-context-files",
        "features-plugins",
      ],
    },
    {
      type: "category",
      label: "Reference",
      collapsed: true,
      items: [
        "cli-commands",
        "references-slash-commands",
        "tools-reference",
        "configuration-reference",
      ],
    },
    {
      type: "category",
      label: "Help",
      collapsed: true,
      items: [
        "examples",
        "troubleshooting",
        "wsl-smoke-test",
        "faq",
        "about",
      ],
    },
  ],
};

export default sidebars;
