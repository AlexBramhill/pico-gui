from spatial.classes import Cell, Range
from spatial.props import GridProps
from math import ceil, floor


class GridCellRangeCalculator:
    @staticmethod
    def __get_cell_ranges(axis, props: GridProps, parent_cell: Cell):
        is_x_spacing_values = axis == 'x'
        values = props.x_spacing_values if is_x_spacing_values else props.y_spacing_values
        start_bounds = parent_cell.left_bounds if is_x_spacing_values else parent_cell.top_bounds
        length = parent_cell.width if is_x_spacing_values else parent_cell.height

        print(f'values: {values}, start_bounds: {
              start_bounds}, length: {length}'
              )
        sorted_values = sorted(values)

        if sorted_values[0] != 0:
            sorted_values.insert(0, 0)

        if sorted_values[-1] != length:
            sorted_values.append(length)

        # We know these are an int at this point due to the check for 'absolute_summation'
        ranges = [
            Range(int(start_bounds + sorted_values[i]),
                  int(start_bounds + sorted_values[i + 1]))
            for i in range(len(sorted_values) - 1)
        ]

        return GridCellRangeCalculator.__adjustRangesForMargin(ranges, props)

    @staticmethod
    def __adjustRangesForMargin(ranges: list[Range], props: GridProps) -> list[Range]:
        adjusted_ranges = []
        # print('adjusting ranges')
        # print(f'margin: {props.margin}')
        # [print(f'range: {range}') for range in ranges]

        def reduce_range_by_margin_at_front(range: Range, margin_multiplier: float):
            return Range(
                range.start + (floor(margin_multiplier *
                               props.margin)),
                range.end
            )

        def reduce_range_by_margin_at_end(range: Range, margin_multiplier: float):
            return Range(
                range.start,
                range.end - (ceil(margin_multiplier *
                             props.margin))
            )

        for i in range(len(ranges)):
            current_range = ranges[i]
            is_last = i == len(ranges) - 1
            is_first = i == 0

            if not is_last:
                current_range = reduce_range_by_margin_at_end(
                    current_range, 0.5)
            if not is_first:
                current_range = reduce_range_by_margin_at_front(
                    current_range, 0.5)

            adjusted_ranges.append(current_range)

        # [print(f'adjusted range: {range}') for range in adjusted_ranges]
        return adjusted_ranges

    @staticmethod
    def compute_grid_ranges(props: GridProps, parent_cell: Cell):
        if (props.spacing_type != 'absolute_summation'):
            raise ValueError(
                f"Cannot create cells for display grid. Unsupported division type: {
                    props.spacing_type}"
            )
        print(f'{props.spacing_type, props.x_spacing_values,
              props.y_spacing_values}'
              )
        x_cell_ranges = GridCellRangeCalculator.__get_cell_ranges(
            'x', props, parent_cell)
        y_cell_ranges = GridCellRangeCalculator.__get_cell_ranges(
            'y', props, parent_cell)

        return x_cell_ranges, y_cell_ranges
