import { fetchBaseQuery } from "@reduxjs/toolkit/query/react";

const BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "/api";

console.log("API Base URL:", BASE_URL);

export const baseQuery = () => {
  return fetchBaseQuery({
    baseUrl: BASE_URL,
    prepareHeaders: (headers) => {
      headers.set("Content-Type", "application/json");
      return headers;

      //   const token = (getState() as RootState).auth.token;
      // If we have a token set in state, let's assume that we should be passing it.
      //   if (token) {
      //     headers.set("authorization", `Bearer ${token}`);
      //   }
      //   return headers;
    },
  });
};
