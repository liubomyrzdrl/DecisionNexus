import AlertsList from "@/components/alerts/AlertsList";
import AlertHeader from "@/components/alerts/AlertHeader";

const AlertLayout = ({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) => {
  return (
    <div>
      <AlertHeader />
      <div className="flex gap-4">
        <aside className="w-1/3">
          <AlertsList /> {/* Ваш список алертів тут */}
        </aside>
        <section className="flex-1">
          {children} {/* Тут з'являтиметься AlertDetails при кліку */}
        </section>
      </div>
    </div>
  );
};

export default AlertLayout;
