import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardFooter } from "@/components/ui/card";
import { Field, FieldGroup } from "@/components/ui/field";

import { toast } from "sonner";

import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";

import SelectFormField from "@/components/Form/SelectFormField";
import InputFormField from "@/components/Form/InputFormField";
import TextAreaFormField from "@/components/Form/TextAreaFormField";
import { useCreateAlertMutation } from "@/api/alerts";
import { SEVERITY_OPTIONS, SOURCE_OPTIONS } from "@/constants";

// AlertStatus = Literal["new", "in_progress", "resolved", "closed"]
// AlertSource = Literal["manual", "monitoring", "ai_detected", "logs", "external", "integration"]
// AlertSeverity = Literal["low", "medium", "high", "critical"]
const createAlertsDialogSchema = z.object({
  title: z
    .string()
    .min(5, "Bug title must be at least 5 characters.")
    .max(32, "Bug title must be at most 32 characters."),
  description: z
    .string()
    .min(20, "Description must be at least 20 characters.")
    .max(100, "Description must be at most 100 characters."),
  severity: z.enum(["low", "medium", "high", "critical"], {
    message: "Please select a severity level.",
  }),
  source: z.enum(
    ["manual", "monitoring", "ai_detected", "logs", "external", "integration"],
    {
      message: "Please select a source.",
    },
  ),
  category: z
    .string()
    .max(50, "Category must be at most 50 characters.")
    .optional(),
});

type CreateAlertsDialogType = z.infer<typeof createAlertsDialogSchema>;

type CreateAlertsDialogPropsType = {
  open: boolean;
  setOpen: (open: boolean) => void;
};

const CreateAlertsDialog = ({ open, setOpen }: CreateAlertsDialogPropsType) => {
  const form = useForm<z.infer<typeof createAlertsDialogSchema>>({
    resolver: zodResolver(createAlertsDialogSchema),
    defaultValues: {
      title: "",
      description: "",
      severity: "low",
      source: "manual",
      category: "",
    },
  });

  const [createAlertProcess] = useCreateAlertMutation();

  const onSubmit = (data: CreateAlertsDialogType) => {
    console.log("Data", data);
    try {
      createAlertProcess(data).unwrap();
      toast.success("Alert created successfully.");
      form.reset();
      setOpen(false);
    } catch (error) {
      toast.error(
        `Failed to create alert. Please try again. - ${error instanceof Error ? error.message : "Unknown error"}`,
      );
    }
  };

  return (
    <Dialog open={open}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Create New alert</DialogTitle>
          <DialogDescription className="text-muted-foreground">
            Fill in the details to create a new alert
          </DialogDescription>
        </DialogHeader>
        <Card className="w-full sm:max-w-md">
          <CardContent>
            <form id="form-rhf-demo" onSubmit={form.handleSubmit(onSubmit)}>
              <FieldGroup>
                <InputFormField
                  form={form}
                  name="title"
                  label="Title"
                  placeholder="title"
                />
                <TextAreaFormField
                  form={form}
                  name="description"
                  label="Description"
                  placeholder="I'm having an issue with the login button on mobile."
                  description="Include steps to reproduce, expected behavior, and what actually happened."
                />

                <SelectFormField
                  form={form}
                  name="severity"
                  label="Severity"
                  options={SEVERITY_OPTIONS}
                />
                <SelectFormField
                  form={form}
                  name="source"
                  label="Source"
                  options={SOURCE_OPTIONS}
                />
                <InputFormField
                  form={form}
                  name="category"
                  label="Category"
                  placeholder="Category"
                />
              </FieldGroup>
            </form>
          </CardContent>
          <CardFooter>
            <Field orientation="horizontal" className="justify-center gap-2">
              <Button type="submit" form="form-rhf-demo">
                Submit
              </Button>
              <Button
                type="button"
                variant="outline"
                onClick={() => {
                  form.reset();
                  setOpen(false);
                }}
              >
                Закрити
              </Button>
            </Field>
          </CardFooter>
        </Card>
      </DialogContent>
    </Dialog>
  );
};

export default CreateAlertsDialog;
