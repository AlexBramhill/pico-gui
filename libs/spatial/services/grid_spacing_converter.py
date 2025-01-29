from spatial.classes import Cell
from spatial.consts import SpacingType
from spatial.props import GridProps


class GridSpacingConverter:
    """
    Converts the spacing type of a grid to another spacing type
    """
    @staticmethod
    def __convert_non_summation_to_summation(axis, props: GridProps) -> list[int] | list[float | int]:
        is_x = axis == 'x'
        values = props.x_spacing_values if is_x else props.y_spacing_values

        summations = []
        for i in range(len(values)):
            summations.append(sum(values[:i+1]))
        return summations

    @staticmethod
    def __convert_percentage_to_absolute(axis, parent_cell: Cell, props: GridProps) -> list[int]:
        is_x = axis == 'x'
        length = parent_cell.width if is_x else parent_cell.height
        values = props.x_spacing_values if is_x else props.y_spacing_values
        print(f'values: {values}, length: {length}')
        return [round(length * value) for value in values]

    @staticmethod
    def convert_spacing_type(target_spacing_type: str, parent_cell: Cell, props: GridProps):
        current_spacing_type = props.spacing_type

        if current_spacing_type == target_spacing_type:
            return props

        if target_spacing_type != SpacingType.ABSOLUTE_SUMMATION:
            raise NotImplementedError(
                f"Unsupported target division type: {target_spacing_type}")

        if current_spacing_type == SpacingType.PERCENTAGE:
            # The below is a two-step process and should be reduced to
            # a single step in the future
            percentage_summation_x_spacing_values = GridSpacingConverter.__convert_non_summation_to_summation(
                'x', props)
            percentage_summation_y_spacing_values = GridSpacingConverter.__convert_non_summation_to_summation(
                'y', props)

            return GridSpacingConverter.convert_spacing_type(
                SpacingType.ABSOLUTE_SUMMATION, parent_cell, GridProps(
                    spacing_type=SpacingType.PERCENTAGE_SUMMATION,
                    x_spacing_values=percentage_summation_x_spacing_values,
                    y_spacing_values=percentage_summation_y_spacing_values,
                    margin=props.margin
                ))

        elif current_spacing_type == SpacingType.PERCENTAGE_SUMMATION:
            new_x_spacing_values = GridSpacingConverter.__convert_percentage_to_absolute(
                'x', parent_cell, props)
            new_y_spacing_values = GridSpacingConverter.__convert_percentage_to_absolute(
                'y', parent_cell, props)

            return GridProps(
                spacing_type=target_spacing_type,
                x_spacing_values=new_x_spacing_values,
                y_spacing_values=new_y_spacing_values,
                margin=props.margin
            )

        elif current_spacing_type == SpacingType.ABSOLUTE:
            new_x_spacing_values = GridSpacingConverter.__convert_non_summation_to_summation(
                'x', props)
            new_y_spacing_values = GridSpacingConverter.__convert_non_summation_to_summation(
                'y', props)

            return GridProps(
                spacing_type=target_spacing_type,
                x_spacing_values=new_x_spacing_values,
                y_spacing_values=new_y_spacing_values,
                margin=props.margin
            )

        raise NotImplementedError(
            f"Unsupported target division type: {target_spacing_type}")
