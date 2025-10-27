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

const shuffle = (array: Array<any>) => {
  return array.sort(() => Math.random() - 0.5);
}

export const websites = await shuffle((await parseResponseJSON(
  await api.get("websites/all")
))) as Array<Website>;
console.log(websites)