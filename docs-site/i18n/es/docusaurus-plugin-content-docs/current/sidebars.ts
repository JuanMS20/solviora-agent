import type { SidebarsConfig } from "@docusaurus/plugin-content-docs";

const sidebars: SidebarsConfig = {
  docsSidebar: [
    {
      type: "doc",
      id: "index",
      label: "Inicio",
    },
    {
      type: "category",
      label: "Primeros pasos",
      collapsed: false,
      items: ["quickstart", "installation"],
    },
    {
      type: "category",
      label: "Usar Solviora",
      collapsed: false,
      items: [
        "cli-basics",
        "configuration",
        "providers",
        "tools",
        "skills",
        "profiles",
        "sessions",
        "tui",
        "security",
      ],
    },
    {
      type: "category",
      label: "Referencia",
      collapsed: true,
      items: [
        "cli-commands",
        "tools-reference",
        "configuration-reference",
      ],
    },
    {
      type: "category",
      label: "Ayuda",
      collapsed: true,
      items: [
        "learning-path",
        "examples",
        "troubleshooting",
        "faq",
        "about",
      ],
    },
  ],
};

export default sidebars;
