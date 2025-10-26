import { api } from "./api";

export type Marker = {
  coordinates: Array<number>;
  title: string;
  action: Function;
  id: string;
};

export let websites = await api.get("/websites/all");
