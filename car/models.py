from django.db import models

# Create your models here.
# class Car(models.Model):

#     # Attributes

#     name = models.CharField(max_length=100, blank=False, null=False, unique=True)
#     body = models.CharField(max_length=1000, blank=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nodes')

#     # Methods
    
#     def __str__(self):
#         return self.name
    
#     def save(self, *args, **kwargs):
#         self.full_clean()
#         return super(Node, self).save(*args, **kwargs)

#     def get_child_nodes(self):
#         edges = self.outgoing_edges.all()
#         nodes = map(lambda edge: edge.target, edges)
#         return list(nodes)

#     def get_votes(self):
#         edges = self.incoming_edges.all()
#         sum = 0
#         for edge in edges:
#             sum = sum + edge.votes()
#         return sum
    
#     def get_reports(self):
#         return self.reports.count()

#     def report(self, user):
#         reported = False
#         if not user.nodereports.filter(node=self).exists():
#             NodeReport(node=self, user=user).save()
#             reported = True
#         if self.get_reports() >= DELETE_NODE_REPORTS and \
#             self.get_votes() <= DELETE_NODE_VOTES:
#             self.delete()
#         return reported

#     def connect_with_parent(self, parent):
#         if not self.incoming_edges.filter(source=parent).exists():
#             Edge(source=parent, target=self).save()
    
#     def connect_with_child(self, child):
#         if not self.outgoing_edges.filter(target=child).exists():
#             Edge(source=self, target=child).save()

#     def vote(self, parent, user, voteparam):
#         voted = False
#         if parent and self.incoming_edges.filter(source=parent).exists():
#             edge = self.incoming_edges.filter(source=parent).first()
#             voted = edge.vote(user, voteparam)
#         return voted