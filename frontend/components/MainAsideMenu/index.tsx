import Link from "next/dist/client/link";

const MainAsideMenu = () => (
  <aside className="w-1/6 p-8 border-r border-amber-50">
    <nav className="flex flex-col gap-4">
      <Link href="/" className="text-xl font-bold text-amber-600">
        Dashboards
      </Link>
      <Link href="/alerts" className="text-xl font-bold text-amber-600">
        Alerts  
      </Link>
      <Link href="/incidents" className="text-xl font-bold text-amber-600">
        Incidents
      </Link>
    </nav>
  </aside>
);

export default MainAsideMenu;
