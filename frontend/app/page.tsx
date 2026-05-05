import { Button } from "@/components/ui/button";

export default function Home({ children }: { children: React.ReactNode }) {
  return (
    <div className=" font-sans dark:bg-black ">
      <h1 className="text-amber-50 text-2xl">Dashboards Content</h1>
      <Button className="mt-4 bg-red-400 text-white">Click me</Button>
      <Button
        variant="outline"
        className="mt-4 border-red-400 bg-red-400 text-white hover:bg-red-500 hover:text-white"
      >
        Click me
      </Button>
      {children}
    </div>
  );
}
