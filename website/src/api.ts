import * as config from '../config' 
import ky from 'ky'

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