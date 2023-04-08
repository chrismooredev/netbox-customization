#!/usr/bin/python3

# Produces a sorted list of Racks:
#  - pseudocode: len(rack.images) and rack.images.most_recent.created
#    - Racks without photos will be listed first
#    - Racks with photos will be sorted according to ascending key (most_recent_photo.created)

from extras.reports import Report
from extras.models import ImageAttachment
from dcim.models import Site, Rack

class DeviceConnectionsReport(Report):
    description = "Validate the minimum physical connections for each device"

    def find_rack_images(self):
        images = (ImageAttachment.objects.prefetch(['content_type', 'object_id'])
            .filter(content_type='dcim.rack'))
        racks = list(Rack.objects.all())

        self.log_failure(None, "this script is likely to break!")
