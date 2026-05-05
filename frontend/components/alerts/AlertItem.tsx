import type { AlertSeverity } from "@/types";
import Link from "next/link";

const AlertItem = ({
  id,
  title,
  description,
  severity,
}: {
  id: number;
  title: string;
  description: string;
  severity: AlertSeverity;
}) => {
  return (
    <Link
      href={`/alerts/${id}`}
      className="block border p-4 rounded mb-2 hover:bg-muted"
    >
      <div className="border p-4 rounded mb-2">
        <h2 className="text-xl font-semibold">{title}</h2>
        <p className="text-muted-foreground">{description}</p>
        <p className="text-sm text-muted-foreground">Severity: {severity}</p>
      </div>
    </Link>
  );
};

export default AlertItem;
