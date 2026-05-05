"use client";
import { useState, useEffect } from "react";

import { Button } from "@/components/ui/button";
import { PlusIcon } from "lucide-react";
import Link from "next/link";
import CreateIncidentsDialog from "@/components/incidents/CreateIncidentsDialog";
import { toast } from "sonner";
import { useGetIncidentsQuery } from "@/api/incidents";

const Incidents = () => {
  const [openCreateIncidentDialog, setOpenCreateIncidentDialog] =
    useState(false);
  const { data: incidents, isLoading } = useGetIncidentsQuery();
  return (
    <div className="">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-4xl font-bold tracking-tight">Incidents</h1>
          <div className="text-lg text-muted-foreground">
            Manage and track system incidents and outages
          </div>
        </div>
        <Button
          onClick={() => setOpenCreateIncidentDialog(true)}
          //   onClick={() => toast.success("Вітаю!", { description: "Все працює" })}
        >
          <PlusIcon className="mr-2 h-4 w-4" />
          <span>Create Incidents</span>
        </Button>
      </div>
      <div className="mt-4">
        {isLoading ? (
          <div>Loading...</div>
        ) : (
          <ul>
            {incidents?.map((incident) => (
              <Link
                href={`/incidents/${incident.id}`}
                key={incident.id}
                className="block border p-4 rounded mb-2 hover:bg-muted"
              >
                <li key={incident.id} className="border p-4 rounded mb-2">
                  <h2 className="text-xl font-semibold">{incident.title}</h2>
                  <p className="text-muted-foreground">
                    {incident.description}
                  </p>
                  <p className="text-sm text-muted-foreground">
                    Severity: {incident.severity}
                  </p>
                </li>
              </Link>
            ))}
          </ul>
        )}
      </div>
      <CreateIncidentsDialog
        open={openCreateIncidentDialog}
        setOpen={setOpenCreateIncidentDialog}
      />
    </div>
  );
};

export default Incidents;
