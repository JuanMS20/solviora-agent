import type { SidebarsConfig } from "@docusaurus/plugin-content-docs";

const sidebars: SidebarsConfig = {
  docsSidebar: [
    {
      type: "category",
      label: "Getting Started",
      collapsed: false,
      items: ["quickstart", "installation"],
    },
    {
      type: "category",
      label: "Core Concepts",
      collapsed: false,
      items: [
        "cli-basics",
        "configuration",
        "providers",
        "tools",
        "skills",
      ],
    },
    {
      type: "category",
      label: "Reference",
      collapsed: true,
      items: [
        "cli-commands",
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
