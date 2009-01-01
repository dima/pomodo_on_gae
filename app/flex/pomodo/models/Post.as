package pomodo.models {
  import org.ruboss.models.RubossModel;
  
  [Resource(name="posts")]
  [Bindable]
  public class Post extends RubossModel {
    public static const LABEL:String = "title";

    public var title:String;

    public var content:String;

    public function Post() {
      super(LABEL);
    }
  }
}
