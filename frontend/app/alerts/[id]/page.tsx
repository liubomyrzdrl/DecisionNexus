"use client";

import { use } from "react";
import { useGetAlertByIdQuery } from "@/api/alerts";
const AlertDetails = ({ params }: { params: Promise<{ id: string }> }) => {
  const { id } = use(params);

  const { data: alert } = useGetAlertByIdQuery(+id);
  return (
    <div className="font-bold">
      Alert Details: {id}
      {alert ? (
        <div>
          <h2>{alert?.title}</h2>
          <p>{alert.description} </p>
        </div>
      ) : (
        <div>Alert not found</div>
      )}
    </div>
  );
};

export default AlertDetails;
