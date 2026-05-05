import { createApi } from "@reduxjs/toolkit/query/react";
import { baseQuery } from "@/api/baseQuery";

import type { IncidentType   } from "@/types/incidents";

export const incidentsApi = createApi({
  reducerPath: "incidentsApi",
  tagTypes: ["Incidents", "IncidentID"],
  baseQuery: baseQuery(),
  endpoints: (builder) => ({
    getIncidents: builder.query<IncidentType[], void>({
      query: () => "/incidents",
      providesTags: ["Incidents"],
    }),
    getIncidentById: builder.query<IncidentType, string>({
      query: (id) => `/incidents/${id}`,
      // providesTags: (id) => [{ type: "IncidentID", id }],
      //   providesTags: (result, error, id) => [{ type: "IncidentID", id }],
    }),
    createIncident: builder.mutation({
      query: (newIncident) => ({
        url: "/incident",
        method: "POST",
        body: newIncident,
      }),
      invalidatesTags: ["Incidents"],
    }),
    createIncidentReview: builder.mutation({
      query: ({ incidentId, body }) => ({
        url: `/incidents/${incidentId}/reviews`,
        method: "POST",
        body,
      }),
      invalidatesTags: (result, error, { incidentId }) => [
        { type: "IncidentID", id: incidentId },
      ],
    }),
    getReviewsByIncidentId: builder.query({
      query: (incidentId) => `/incidents/${incidentId}/reviews`,
      providesTags: (result, error, incidentId) => [
        { type: "IncidentID", id: incidentId },
      ],
    }),

    updateIncidentReview: builder.mutation({
      query: ({ incidentId, reviewId, review }) => ({
        url: `/incidents/${incidentId}/reviews/${reviewId}`,
        method: "PATCH",
        body: { review },
      }),
      invalidatesTags: (result, error, { incidentId }) => [
        { type: "IncidentID", id: incidentId },
      ],
    }),
  }),
});

export const {
  useGetIncidentsQuery,
  useGetIncidentByIdQuery,
  useCreateIncidentMutation,
  useCreateIncidentReviewMutation,
  useGetReviewsByIncidentIdQuery,
} = incidentsApi;
