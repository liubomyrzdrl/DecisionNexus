import React from "react";

import { Controller, UseFormReturn, FieldValues, Path } from "react-hook-form";
import { Input } from "@/components/ui/input";

import { Field, FieldError, FieldLabel } from "@/components/ui/field";

type InputFormFieldProps<TFieldValues extends FieldValues> = {
  form: UseFormReturn<TFieldValues>;
  name: Path<TFieldValues>; 
  label: string;
  placeholder?: string;
};

const InputFormField = <TFieldValues extends FieldValues>({
  form,
  name,
  label,
  placeholder,
}: InputFormFieldProps<TFieldValues>) => {
  return (
    <Controller
      name={name}
      control={form.control}
      render={({ field, fieldState }) => (
        <Field data-invalid={fieldState.invalid}>
          <FieldLabel htmlFor={`form-rhf-demo-${name}`}>{label}</FieldLabel>
          <Input
            {...field}
            id={`form-rhf-demo-${name}`}
            aria-invalid={fieldState.invalid}
            placeholder={placeholder}
            autoComplete="off"
          />
          {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
        </Field>
      )}
    />
  );
};

export default InputFormField;
