/**
 * Swizzled LocaleDropdownNavbarItem to fix locale URL generation
 * when trailingSlash: false.
 *
 * Root cause: useAlternatePageUtils.createUrl() computes pathnameSuffix
 * via canonicalPathname.replace(baseUrl, ''). When the current page is
 * the locale root (e.g. /es) and baseUrl has a trailing slash (/es/),
 * the replace fails and pathnameSuffix keeps the locale prefix, producing
 * doubled paths like //es or /es//es.
 *
 * Fix: compute locale URLs directly from localeConfigs baseUrl + the
 * current page suffix (stripped of any locale prefix).
 */
import React from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { translate } from "@docusaurus/Translate";
import {
  mergeSearchStrings,
  useHistorySelector,
} from "@docusaurus/theme-common";
import DropdownNavbarItem from "@theme/NavbarItem/DropdownNavbarItem";
import IconLanguage from "@theme/Icon/Language";
import type { Props } from "@theme/NavbarItem/LocaleDropdownNavbarItem";
import styles from "./styles.module.css";

/**
 * Strip locale prefix from a pathname.
 * /es/docs/quickstart → /docs/quickstart
 * /docs/quickstart    → /docs/quickstart (default locale, no prefix)
 * /es                 → /
 */
function stripLocalePrefix(
  pathname: string,
  localeBaseUrls: Record<string, string>,
): string {
  // Sort by length descending so longer prefixes match first
  const entries = Object.entries(localeBaseUrls).sort(
    ([, a], [, b]) => b.length - a.length,
  );

  for (const [, baseUrl] of entries) {
    if (baseUrl === "/") continue;
    // Handle exact match (e.g. pathname="/es", baseUrl="/es/")
    const noSlash = baseUrl.replace(/\/$/, "");
    if (noSlash && (pathname === noSlash || pathname === baseUrl)) {
      return "/";
    }
    // Handle prefix match (e.g. pathname="/es/docs/quickstart")
    if (pathname.startsWith(baseUrl)) {
      return "/" + pathname.slice(baseUrl.length);
    }
    if (pathname.startsWith(noSlash + "/")) {
      return "/" + pathname.slice(noSlash.length + 1);
    }
  }
  return pathname;
}

/**
 * Normalize a URL path by collapsing duplicate slashes,
 * preserving the pathname:// protocol prefix.
 */
function normalizePath(url: string): string {
  return url.replace(/([^:])\/{2,}/g, "$1/");
}

export default function LocaleDropdownNavbarItem({
  mobile,
  dropdownItemsBefore,
  dropdownItemsAfter,
  queryString,
  ...props
}: Props): JSX.Element {
  const {
    siteConfig,
    i18n: { currentLocale, locales, localeConfigs },
  } = useDocusaurusContext();

  const search = useHistorySelector((history) => history.location.search);
  const hash = useHistorySelector((history) => history.location.hash);

  // Build locale baseUrl map
  const localeBaseUrls: Record<string, string> = {};
  for (const [locale, config] of Object.entries(localeConfigs)) {
    localeBaseUrls[locale] = (config as { baseUrl: string }).baseUrl;
  }

  // Get current pathname
  const pathname =
    typeof window !== "undefined" ? window.location.pathname : "/";

  // Strip the locale prefix to get the page-agnostic suffix
  const pageSuffix = stripLocalePrefix(pathname, localeBaseUrls);

  function getLocaleUrl(locale: string): string {
    const localeConfig = localeConfigs[locale];
    if (!localeConfig) return "pathname:///";
    const isSameDomain =
      (localeConfig as { url?: string }).url === siteConfig.url;
    const baseUrl = (localeConfig as { baseUrl: string }).baseUrl;

    const finalSearch = mergeSearchStrings([search, queryString], "append");

    // Build the target path: baseUrl + pageSuffix, avoiding double slashes
    // at the join point.
    const base = baseUrl.endsWith("/") ? baseUrl : baseUrl + "/";
    const suffix = pageSuffix.startsWith("/") ? pageSuffix.slice(1) : pageSuffix;
    const targetPath = normalizePath(`${base}${suffix}`);

    if (isSameDomain) {
      return `pathname://${targetPath}${finalSearch}${hash}`;
    }
    return `${(localeConfig as { url: string }).url}${targetPath}${finalSearch}${hash}`;
  }

  const localeItems = locales.map((locale) => ({
    label: (localeConfigs[locale] as { label: string }).label || locale,
    lang: (localeConfigs[locale] as { htmlLang: string }).htmlLang || locale,
    to: getLocaleUrl(locale),
    target: "_self" as const,
    autoAddBaseUrl: false,
    className:
      locale === currentLocale
        ? mobile
          ? "menu__link--active"
          : "dropdown__link--active"
        : "",
  }));

  const items = [
    ...(dropdownItemsBefore ?? []),
    ...localeItems,
    ...(dropdownItemsAfter ?? []),
  ];

  const dropdownLabel = mobile
    ? translate({
        message: "Languages",
        id: "theme.navbar.mobileLanguageDropdown.label",
        description: "The label for the mobile language switcher dropdown",
      })
    : translate({
        message: "Languages",
        id: "theme.navbar.mLanguageDropdown.label",
        description: "The label for the language switcher dropdown",
      });

  return (
    <DropdownNavbarItem
      {...props}
      mobile={mobile}
      label={
        <>
          <IconLanguage className={styles.iconLanguage} />
          {dropdownLabel}
        </>
      }
      items={items}
    />
  );
}
