import React from "react";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Controller, UseFormReturn, FieldValues, Path, } from "react-hook-form";

type InputSelectFieldType<TFieldValues extends FieldValues> = {
  form: UseFormReturn<TFieldValues>;
  name: Path<TFieldValues>; 
  label: string;
  placeholder?: string;
  options: { value: string; label: string }[];
};

const SelectFormField = <TFieldValues extends FieldValues>({ form, name, label, options }: InputSelectFieldType<TFieldValues>) => {
  return (
    <Controller
      name={name}
      control={form.control}
      render={({ field }) => (
        <Select {...field}>
          <SelectTrigger className="w-full max-w-48">
            <SelectValue placeholder="Select a severity" />
          </SelectTrigger>
          <SelectContent>
            <SelectGroup>
              <SelectLabel>{label}</SelectLabel>
              {options.map((option) => (
                <SelectItem key={option.value} value={option.value}>
                  {option.label}
                </SelectItem>
              ))}
            </SelectGroup>
          </SelectContent>
        </Select>
      )}
    />
  );
};

export default SelectFormField;


