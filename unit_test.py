import unittest
from pythonic import *


class Test_PyVX_Objects(unittest.TestCase):

    def test_create_context(self):
        ctx = Context()
        references_0 = ctx.get_references()
        image = Image(ctx, 300, 400, vx.DF_IMAGE_U8, 1)
        references_1 = ctx.get_references()
        self.assertEqual(references_0+1, references_1)
        image.vxReleaseImage()
        references_2 = ctx.get_references()
        self.assertEqual(references_0, references_2)
        ctx.release_context()

    def test_create_graph(self):
        ctx = Context()
        graph = Graph(ctx)
        self.assertEqual(0, graph.get_num_node())
        self.assertEqual(0, graph.get_status())
        graph.vxReleaseGraph()
        ctx.release_context()

    def test_create_image(self):
        ctx = Context()
        img_uniform = Image(ctx, 300, 400, vx.DF_IMAGE_U8, 1)
        self.assertEqual(img_uniform.width, img_uniform.get_width())
        self.assertEqual(img_uniform.height, img_uniform.get_height())

        img = Image(ctx, 300, 400, vx.DF_IMAGE_U8)
        self.assertEqual(img.width, img.get_width())
        self.assertEqual(img.height, img.get_height())
        img.vxReleaseImage()
        ctx.release_context()

    def test_graph_with_statement(self):
        with Graph() as g:
            img_uniform = Image(g.context, 300, 400, vx.DF_IMAGE_U8, 1)


# class Test_PyVX_Nodes(unittest.TestCase):
#     def test_sobel_node(self):
#         with Graph() as g:
#             src = vx_utils.read_image(img_path, g.context)
#             x, y = Sobel3x3Node(g, src)
#         g.vxProcessGraph()


if __name__ == "__main__":
    unittest.main(verbosity=2)
