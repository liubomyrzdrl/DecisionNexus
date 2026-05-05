import { configureStore } from "@reduxjs/toolkit";

import { incidentsApi } from "@/api/incidents";
import { alertApi } from "@/api/alerts";

const store = configureStore({
  reducer: {
    [incidentsApi.reducerPath]: incidentsApi.reducer,
    [alertApi.reducerPath]: alertApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(incidentsApi.middleware, alertApi.middleware),
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;
