import type { VisualizationDefinition } from '../../types/api';
import { ArrayHashMapRenderer } from './renderers/ArrayHashMapRenderer';
import { BinaryPartitionRenderer } from './renderers/BinaryPartitionRenderer';

export function VisualizationScene({
  definition,
  stepIndex,
}: {
  definition: VisualizationDefinition;
  stepIndex: number;
}) {
  switch (definition.renderer) {
    case 'array-hash-map': {
      const step = definition.steps[stepIndex];
      return (
        <ArrayHashMapRenderer
          definition={definition}
          step={step}
          previousStep={stepIndex > 0 ? definition.steps[stepIndex - 1] : null}
        />
      );
    }
    case 'binary-partition': {
      const step = definition.steps[stepIndex];
      return (
        <BinaryPartitionRenderer
          definition={definition}
          step={step}
          previousStep={stepIndex > 0 ? definition.steps[stepIndex - 1] : null}
        />
      );
    }
  }
}
