import type { SidebarsConfig } from "@docusaurus/plugin-content-docs";

const sidebars: SidebarsConfig = {
  docsSidebar: [
    {
      type: "category",
      label: "Primeros pasos",
      collapsed: false,
      items: ["quickstart", "installation"],
    },
    {
      type: "category",
      label: "Conceptos principales",
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
        "examples",
        "troubleshooting",
        "faq",
        "about",
      ],
    },
  ],
};

export default sidebars;
