"use client";

import { useState } from "react";

import { Button } from "@/components/ui/button";
import { PlusIcon } from "lucide-react";
import CreateAlertsDialog from "@/components/alerts/CreateAlertDialog";

const AlertHeader = () => {
  const [openCreateAlertDialog, setOpenCreateAlertDialog] = useState(false);
  return (
    <div className="flex justify-between items-center">
      <div>
        <h1 className="text-4xl font-bold tracking-tight">Alerts</h1>
        <div className="text-lg text-muted-foreground">
          Manage and track system alerts and notifications
        </div>
      </div>
      <Button onClick={() => setOpenCreateAlertDialog(true)}>
        <PlusIcon className="mr-2 h-4 w-4" />
        <span>Create Alerts</span>
      </Button>
      <CreateAlertsDialog
        open={openCreateAlertDialog}
        setOpen={setOpenCreateAlertDialog}
      />
    </div>
  );
};

export default AlertHeader;
