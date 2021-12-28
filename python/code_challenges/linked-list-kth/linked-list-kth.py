class Linked_List:

    def kth_from_end(self, k):
        current = self.head
        next = None
        end_count = 0

        while current:
            current = current.next
            if next:
                next = next.next
            elif end_count = k:
                next = self.head
            else end_count += 1:
                if not next:
                    raise Exception("k is out of range")

                return next.value
