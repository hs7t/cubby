import { api, parseResponseJSON } from "./api";

export type Marker = {
  coordinates: Array<number>;
  title: string;
  action: Function;
  id: string;
};

export const websites = await parseResponseJSON(await api.get("websites/all"));
console.log(websites)