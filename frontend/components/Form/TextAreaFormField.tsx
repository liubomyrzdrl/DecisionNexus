import React from "react";
import { Controller, FieldValues, Path, UseFormReturn } from "react-hook-form";

import {
  InputGroup,
  InputGroupAddon,
  InputGroupText,
  InputGroupTextarea,
} from "@/components/ui/input-group";
import {
  Field,
  FieldError,
  FieldLabel,
  FieldDescription,
} from "@/components/ui/field";

type InputFormFieldPropsType<TFieldValues extends FieldValues> = {
  form: UseFormReturn<TFieldValues>;
  name: Path<TFieldValues>;
  label: string;
  placeholder?: string;
  description?: string;
};

const TextAreaFormField = <TFieldValues extends FieldValues>({
  form,
  name,
  label,
  placeholder,
  description,
}: InputFormFieldPropsType<TFieldValues>) => {
  return (
    <Controller
      name={name}
      control={form.control}
      render={({ field, fieldState }) => (
        <Field data-invalid={fieldState.invalid}>
          <FieldLabel htmlFor={`form-rhf-demo-${name}`}>{label}</FieldLabel>
          <InputGroup>
            <InputGroupTextarea
              {...field}
              id={`form-rhf-demo-${name}`}
              placeholder={placeholder}
              rows={6}
              className="min-h-24 resize-none"
              aria-invalid={fieldState.invalid}
            />
            <InputGroupAddon align="block-end">
              <InputGroupText className="tabular-nums">
                {field.value.length}/100 characters
              </InputGroupText>
            </InputGroupAddon>
          </InputGroup>
          <FieldDescription>{description}</FieldDescription>
          {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
        </Field>
      )}
    />
  );
};

export default TextAreaFormField;
