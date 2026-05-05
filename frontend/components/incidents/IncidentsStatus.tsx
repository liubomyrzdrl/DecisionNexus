import { cn } from '@/lib/utils';
import React from 'react';



type SourceType =
  | "manual"        // створив користувач
  | "alert"         // з monitoring system
  | "ai_detected"   // AI знайшов anomaly
  | "log"           // з логів
  | "external"      // клієнт / користувач повідомив
  | "integration"   // з іншого сервісу (Slack, PagerDuty)

type StatusType = "open" | "in_progress" | "resolved" | "closed";



type SeverityType = "low" | "medium" | "high" | "critical";

type CategoryType = string;
type IncidentsBadgePropsType = {  
    type: SourceType | SeverityType | StatusType | CategoryType;
    content: string;
};


const sourceOptions: Record<string, string> = {
    manual: "bg-blue-100 text-blue-800",
    alert: "bg-yellow-100 text-yellow-800",
    ai_detected: "bg-purple-100 text-purple-800",
    log: "bg-green-100 text-green-800",
    external: "bg-red-100 text-red-800",
    integration: "bg-gray-100 text-gray-800",
};

const severityOptions: Record<string, string> = {
    low: "bg-green-100 text-green-800",
    medium: "bg-yellow-100 text-yellow-800",
    high: "bg-orange-100 text-orange-800",
    critical: "bg-red-100 text-red-800",
};

const statusOptions: Record<string, string> = {
    open: "bg-blue-100 text-blue-800",
    in_progress: "bg-purple-100 text-purple-800",
    resolved: "bg-green-100 text-green-800",
    closed: "bg-gray-100 text-gray-800",
};


const IncidentsBadge = ({ type, content }: IncidentsBadgePropsType) => {
    return (
        <div className="max-w-25">
            <div className="font-semibold text-slate-600 text-center">{type}</div>
            <div className={cn("px-2 py-1 rounded-[15px] mt-2 p-2 text-xs font-medium text-center", sourceOptions[type] || severityOptions[type] || statusOptions[type] || "bg-gray-100 text-gray-800")}>
                {content}
            </div>
        </div>
    );
};

export default IncidentsBadge;