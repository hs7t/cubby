import { api, parseResponseJSON } from "./api";

export type Marker = {
  coordinates: Array<number>;
  title: string;
  action: Function;
  id: string;
};

export let websites = await parseResponseJSON(await api.get("websites/all"));
console.log(websites)