import type { ServerResponse } from 'http';
import * as config from '../config' 
import ky, { type KyResponse } from 'ky'

export const api = ky.create({
  prefixUrl: config.API_URL,
  timeout: 10000,
  hooks: {
    beforeError: [
      (error) => {
        console.error("API Error:", error);
        return error;
      },
    ],
  },
});

export const parseResponseJSON = async (requestResponse: KyResponse) => {
  return JSON.parse(JSON.stringify(await requestResponse.json()));
};