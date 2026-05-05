"use client";

import { use, useState } from "react";
import Link from "next/link";
import { ArrowLeftCircleIcon, Share2Icon } from "lucide-react";

import { useGetIncidentByIdQuery, useCreateIncidentMutation, useGetReviewsByIncidentIdQuery } from "@/api/incidents";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import CreateIncidentReviewDialog from "@/components/incidents/CreateIncidentReviewDialog";
import IncidentsBadge from "@/components/incidents/IncidentsStatus";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import type { IncidentReviewType } from "@/types";
// import { Spinner } from "@/components/ui/Spinner";

const IncidentPage = ({ params }: { params: Promise<{ id: string }> }) => {
  const [openCreateReviewDialog, setOpenCreateReviewDialog] = useState(false);
  const resolvedParams = use(params);
  const id = resolvedParams.id;
  const { data } = useGetIncidentByIdQuery(id);
  const { data: reviews } = useGetReviewsByIncidentIdQuery(id);


  console.log("Incident Data:", data);
    console.log("Incident Data:", reviews);
  return (
    <main>
      <div className="flex justify-between items-center">
        <div className="flex justify-between items-center gap-x-2">
          <Link href="/incidents">
            <ArrowLeftCircleIcon className="mr-2" />
          </Link>
          <div className="mb-4">
            <h3 className="text-4xl font-bold tracking-tight">
              Incident Details
            </h3>
            <div className="text-lg text-muted-foreground">
              View and manage details of the selected incident
            </div>
          </div>
        </div>

        <div className="ml-auto">
          <Share2Icon className="mr-2" />
        </div>
      </div>
      {/* <div>
        <Button onClick={() => setOpenCreateReviewDialog(true)}>
          Make Review
        </Button>
      </div> */}
      <Card className=" w-full">
        <CardContent>
          <h1 className="text-2xl font-semibold">
            {" "}
            <span className="mr-2">#</span>
            {data?.title}
          </h1>
          <p className="text-muted-foreground mt-2">{data?.description}</p>
          <div className=" flex gap-x-4 mt-4">
            <IncidentsBadge type="severity" content={data?.severity ?? ""} />
            <IncidentsBadge type="source" content={data?.source ?? ""} />
            <IncidentsBadge type="status" content={data?.status ?? ""} />
            <IncidentsBadge type="category" content={data?.category ?? "-"} />
          </div>
        </CardContent>
      </Card>
      <Card className=" w-full mt-4">
        <Button onClick={() => setOpenCreateReviewDialog(true)} className="w-37 ml-auto mb-4">
          Add Review
        </Button>
        <CardContent>
          <h2 className="text-xl font-semibold mb-2">Reviews</h2>
          {reviews && reviews.length > 0  ? (
            <Accordion  className="w-full">
              {reviews.map((review: IncidentReviewType) => (
                <AccordionItem key={review.id} value={`item-${review.id}`}>
                  <AccordionTrigger>
                    <div className="flex flex-col items-start">
                      <span className="font-medium">Review #{review.id}</span>
                      <span className="text-sm text-muted-foreground">
                        {review.created_at ? new Date(review.created_at).toLocaleDateString() : "N/A"}
                      </span>
                    </div>
                  </AccordionTrigger>
                  <AccordionContent>
                    <div className="space-y-4">
                      <div>
                        <h3 className="font-semibold mb-1">What happened?</h3>
                        <p className="text-muted-foreground">{review.what_happened}</p>
                      </div>
                      <div>
                        <h3 className="font-semibold mb-1">What went wrong?</h3>
                        <p className="text-muted-foreground">{review.what_went_wrong}</p>
                      </div>
                      <div>
                        <h3 className="font-semibold mb-1">Analysis</h3>
                        <p className="text-muted-foreground">{review.analysis}</p>
                      </div>
                      <div>
                        <h3 className="font-semibold mb-1">Recommendations</h3>
                        <p className="text-muted-foreground">{review.recommendations}</p>
                      </div>
                    </div>
                  </AccordionContent>
                </AccordionItem>
              ))}
            </Accordion>    
          ) : <>No reviews found.</> }
        </CardContent>
      </Card>
      <CreateIncidentReviewDialog
        open={openCreateReviewDialog}
        setOpen={setOpenCreateReviewDialog}
        incidentId={id}
      />
    </main>
  );
};

export default IncidentPage;
