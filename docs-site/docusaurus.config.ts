import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";
import { themes as prismThemes } from "prism-react-renderer";

const config: Config = {
  title: "Solviora Agent",
  tagline: "Terminal-first AI agent for developers",
  favicon: "img/favicon.ico",
  url: "https://docs.solviora.dev",
  baseUrl: "/",
  trailingSlash: false,

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  i18n: {
    defaultLocale: "en",
    locales: ["en", "es"],
    localeConfigs: {
      en: { label: "English", direction: "ltr" },
      es: { label: "Español", direction: "ltr" },
    },
  },

  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: "./sidebars.ts",
          editUrl: "https://github.com/solviora/solviora-agent/tree/main/docs-site/",
          showLastUpdateTime: true,
        },
        blog: false,
        theme: {
          customCss: "./src/css/custom.css",
        },
      } satisfies Preset.Options,
    ],
  ],

  plugins: [
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      {
        indexDocs: true,
        indexBlog: false,
        indexPages: true,
        language: ["en", "es"],
        hashed: true,
        explicitSearchResultPath: true,
        searchResultLimits: 8,
        searchContextByPaths: [
          { label: "Docs", path: "docs" },
        ],
      },
    ],
    [
      "@docusaurus/plugin-ideal-image",
      {
        quality: 80,
        max: 1200,
        min: 480,
        steps: 3,
        disableInDev: false,
      },
    ],
  ],

  themeConfig: {
    image: "img/og-card.png",
    colorMode: {
      defaultMode: "light",
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
    announcementBar: {
      id: "beta",
      content:
        '🚧 Solviora Agent is in early development. <a href="/docs/about">Learn more</a>',
      backgroundColor: "#26251e",
      textColor: "#faf9f6",
      isCloseable: true,
    },
    navbar: {
      title: "Solviora",
      logo: {
        alt: "Solviora Logo",
        src: "img/logo.svg",
        srcDark: "img/logo-dark.svg",
      },
      items: [
        {
          type: "docSidebar",
          sidebarId: "docsSidebar",
          position: "left",
          label: "Docs",
        },
        {
          type: "localeDropdown",
          position: "right",
          dropdownItemsBefore: [],
          dropdownItemsAfter: [],
          className: "navbar__item--languages",
        },
        {
          href: "https://github.com/solviora/solviora-agent",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Documentation",
          items: [
            { label: "Quickstart", to: "/docs/quickstart" },
            { label: "Installation", to: "/docs/installation" },
            { label: "Configuration", to: "/docs/configuration" },
          ],
        },
        {
          title: "Community",
          items: [
            { label: "GitHub", href: "https://github.com/solviora/solviora-agent" },
            { label: "Discord", href: "https://discord.gg/solviora" },
          ],
        },
        {
          title: "More",
          items: [
            { label: "About", to: "/docs/about" },
            { label: "License (MIT)", to: "/docs/about#license" },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Solviora. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.nightOwlLight,
      darkTheme: prismThemes.nightOwl,
      additionalLanguages: ["bash", "python", "yaml", "json", "toml", "diff"],
    },
    // Search provided by @easyops-cn/docusaurus-search-local (no Algolia config needed)
  } satisfies Preset.ThemeConfig,
};

export default config;
