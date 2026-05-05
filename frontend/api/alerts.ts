import { createApi } from "@reduxjs/toolkit/query/react";

import { baseQuery } from "@/api/baseQuery";
import type { AlertType } from "@/types";

export const alertApi = createApi({
    reducerPath: "alertApi",    
    baseQuery:       baseQuery(),
    tagTypes: ["Alerts", "AlertID"],
    endpoints: (builder) => ({
        getAlerts: builder.query<AlertType[], null>({
            query: () => "/alerts",
            providesTags: ["Alerts"],
        }),
        getAlertById: builder.query<AlertType, number>({
            query: (id) => `/alerts/${id}`,
            providesTags: ["AlertID"],
        }),
        createAlert: builder.mutation< Partial<AlertType>, AlertType>({
            query: (newAlert) => ({
                url: "/alerts",
                method: "POST",
                body: newAlert,
            }),
            invalidatesTags: ["Alerts", "AlertID"],
        }),
    }),
});

export const { useGetAlertsQuery, useGetAlertByIdQuery, useCreateAlertMutation } = alertApi;