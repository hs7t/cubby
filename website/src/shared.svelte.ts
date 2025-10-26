import { api, parseResponseJSON } from "./api";

export type Marker = {
  coordinates: Array<number>;
  title: string;
  action: Function;
  id: string;
};

type Website = {
  cubbyId: string;
  name: string;
  url: string;
  address: string;
  mapCoordinates: Array<number>;
};

export const websites = (await parseResponseJSON(
  await api.get("websites/all")
)) as Array<Website>;
console.log(websites)