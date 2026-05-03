/// <reference types="@docusaurus/module-type-aliases" />
declare module "@docusaurus/plugin-ideal-image" {
  type Props = {
    src: string;
    alt?: string;
    width?: number;
    height?: number;
  };
  export default function IdealImage(props: Props): JSX.Element;
}
