export type AlertStatus = "new" | "in_progress" | "resolved" | "closed";
export type AlertSource =
  | "manual"
  | "monitoring"
  | "ai_detected"
  | "logs"
  | "external"
  | "integration";

  export type AlertSeverity = "low" | "medium" | "high" | "critical";

export type AlertType = {
  id?: string;
  title: string;
  description: string;
  severity: AlertSeverity;
  category?: string;
  status?: AlertStatus;
  signal_data?: Record<string, unknown>;
  source?: AlertSource;
  created_at?: string;
  updated_at?: string;
};




