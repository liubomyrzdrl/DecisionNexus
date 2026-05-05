"use client";

import { useGetAlertsQuery } from "@/api/alerts";
import AlertItem from "@/components/alerts/AlertItem";

const AlertList = () => {
  const { data: alerts, isLoading } = useGetAlertsQuery(null);

  console.log("Alerts data:", alerts);
  return (
    <div>
      <section className="mt-4">
        {isLoading ? (
          <div>Loading...</div>
        ) : (
          <div>
            {alerts?.map(
              (alert) =>
                alert.id && (
                  <AlertItem
                    key={alert.id}
                    id={+alert.id}
                    title={alert.title}
                    description={alert.description}
                    severity={alert.severity}
                  />
                ),
            )}
          </div>
        )}
      </section>
    </div>
  );
};

export default AlertList;
