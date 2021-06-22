from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import ValidationError

from cycle import EndPoints
from cycle.constants import Frame, HandleType, SeatType, Wheel
from cycle.form_utils import create_validation_error_msg
from cycle.mapping import frame_dict, seat_dict, handle_dict, wheel_dict
from cycle.serializer import PriceList


class CyclePricing(ViewSet):
    @action(
        methods=["post"],
        detail=False,
        url_name=EndPoints.PRICE.name,
        url_path=EndPoints.PRICE.value,
    )
    def pricing_list(self, request: Request):
        """

        :param request:
        :return:
        """
        serializer = PriceList()
        serializer.get_data(request=request)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            # Creates a message consisting of missing fields that will be shown in the dashboard pop-up.
            error_message = create_validation_error_msg(fields=serializer.errors.keys())
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={"message": error_message})

        frame_type = serializer.validated_data['frame_type']
        handle_type = serializer.validated_data['handle_type']
        seat_type = serializer.validated_data['seat_type']
        wheel_type = serializer.validated_data['wheel_type']

        final_price = 0.0
        if frame_type not in [frame.name for frame in Frame]:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={"message": f"{frame_type} is not available"})
        if handle_type not in [handle.name for handle in HandleType]:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={"message": f"{handle_type} is not available"})
        if seat_type not in [seat.name for seat in SeatType]:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={"message": f"{seat_type} is not available"})
        if wheel_type not in [wheel.name for wheel in Wheel]:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={"message": f"{wheel_type} is not available"})

        final_price = frame_dict.get(str(frame_type)) + seat_dict.get(str(seat_type)) + handle_dict.get(
            str(handle_type)) + wheel_dict.get(str(wheel_type))
        print(final_price)
        return Response(data={"Price": str(final_price)}, status=status.HTTP_200_OK)
