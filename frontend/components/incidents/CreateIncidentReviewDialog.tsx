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

import SelectSeverity from "@/components/Form/SelectFormField";
import InputFormField from "@/components/Form/InputFormField";
import TextAreaFormField from "@/components/Form/TextAreaFormField";
import { useCreateIncidentReviewMutation } from "@/api/incidents";

const createIncidentReviewDialogSchema = z.object({
  what_happened: z
    .string()
    .min(10, "Bug title must be at least 10 characters.")
    .max(100, "Bug title must be at most 100 characters."),
  what_went_wrong: z
    .string()
    .min(10, "Description must be at least 10 characters.")
    .max(100, "Description must be at most 100 characters."),
  analysis: z
    .string()
    .min(10, "Description must be at least 10 characters.")
    .max(100, "Description must be at most 100 characters."),
  recommendations: z
    .string()
    .min(10, "Description must be at least 10 characters.")
    .max(100, "Description must be at most 100 characters."),
});

type CreateIncidentReviewDialogType = z.infer<
  typeof createIncidentReviewDialogSchema
>;

type CreateIncidentReviewDialogPropsType = {
  open: boolean;
  setOpen: (open: boolean) => void;
  incidentId: string;
};

const CreateIncidentReviewDialog = ({
  open,
  setOpen,
  incidentId,
}: CreateIncidentReviewDialogPropsType) => {
  const form = useForm<z.infer<typeof createIncidentReviewDialogSchema>>({
    resolver: zodResolver(createIncidentReviewDialogSchema),
    defaultValues: {
      what_happened: "",
      what_went_wrong: "",
      analysis: "",
      recommendations: "",
    },
  });


  const [createIncidentReviewProcess] = useCreateIncidentReviewMutation();

  const userId = 1; // Replace with actual user ID from auth context or state

  const onSubmit = async (data: CreateIncidentReviewDialogType) => {
    console.log("Data", data);
    try {
      if (!incidentId) {
        toast.error("Incident ID is missing. Please try again.");
        return;
      }

      if (
        !data.what_happened ||
        !data.what_went_wrong ||
        !data.analysis ||
        !data.recommendations
      ) {
        toast.error("All fields are required. Please fill in all the details.");
        return;
      }

      await createIncidentReviewProcess({ incidentId, body: data }).unwrap();
      toast.success("Incident created successfully.");
      form.reset();
      setOpen(false);
    } catch (error) {
      toast.error(
        `Failed to create incident. Please try again. - ${error instanceof Error ? error.message : "Unknown error"}`,
      );
    }
  };

  return (
    <Dialog open={open}>
      <DialogContent className=" h-[90%] w-30% sm:w-[50%]">
        <DialogHeader>
          <DialogTitle>Create New Incident</DialogTitle>
          <DialogDescription className="text-muted-foreground">
            Fill in the details to create a new incident
          </DialogDescription>
        </DialogHeader>
        <Card className="w-full sm:max-w-md">
          <CardContent className="overflow-auto">
            <form id="form-rhf-demo" onSubmit={form.handleSubmit(onSubmit)}>
              <FieldGroup>
                {/* <InputFormField
                  form={form}
                  name="title"
                  label="Title"
                  placeholder="title"
                /> */}
                <TextAreaFormField
                  form={form}
                  name="what_happened"
                  label="What happened?"
                  placeholder="I'm having an issue with the login button on mobile."
                  description="Include steps to reproduce, expected behavior, and what actually happened."
                />
                <TextAreaFormField
                  form={form}
                  name="what_went_wrong"
                  label="What went wrong?"
                  placeholder="I'm having an issue with the login button on mobile."
                  description="Include steps to reproduce, expected behavior, and what actually happened."
                />
                <TextAreaFormField
                  form={form}
                  name="analysis"
                  label="Analysis"
                  placeholder="I'm having an issue with the login button on mobile."
                  description="Include steps to reproduce, expected behavior, and what actually happened."
                />
                <TextAreaFormField
                  form={form}
                  name="recommendations"
                  label="Recommendations"
                  placeholder="I'm having an issue with the login button on mobile."
                  description="Include steps to reproduce, expected behavior, and what actually happened."
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

export default CreateIncidentReviewDialog;
