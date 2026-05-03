/**
 * Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.
 *
 * Swizzled AnnouncementBar/Content to support i18n translation.
 */
import React from "react";
import clsx from "clsx";
import { useThemeConfig } from "@docusaurus/theme-common";
import { translate } from "@docusaurus/Translate";
import styles from "./Content.styles.module.css";

export default function AnnouncementBarContent(props) {
  const { announcementBar } = useThemeConfig();
  const content = translate({
    id: "announcementBar.content",
    message: announcementBar.content,
    description: "The announcement bar content",
  });

  return (
    <div
      {...props}
      className={clsx(styles.content, props.className)}
      dangerouslySetInnerHTML={{ __html: content }}
    />
  );
}
