export type IncidentType = {
  id: string;
  title: string;
  description: string;
  severity: "low" | "medium" | "high";
  status: "open" | "in_progress" | "resolved";
  category: string;
  source: string;
  analysis: string;
  created_at: string; // ISO date string
  updated_at: string; // ISO date string
};  

export type IncidentReviewType = {
  id: string;
  incident_id: string;
  what_happened: string;
  what_went_wrong: string;
  analysis: string;
  recommendations: string;
  created_at?: string; // ISO date string
  updated_at?: string; // ISO date string
};

