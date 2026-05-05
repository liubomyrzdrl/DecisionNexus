'use client';

import { Provider } from "react-redux";
import { ThemeProvider as NextThemesProvider } from "next-themes"
import store from "@/store";

export const  ReduxProvider = ({ children }: { children: React.ReactNode }) => {
  return <Provider store={store}>{children}</Provider>;
}


 
export const ThemeProvider = ({
  children,
  ...props
}: React.ComponentProps<typeof NextThemesProvider>) => {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}