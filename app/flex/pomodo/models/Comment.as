package pomodo.models {
  import org.ruboss.models.RubossModel;
  
  [Resource(name="comments")]
  [Bindable]
  public class Comment extends RubossModel {
    public static const LABEL:String = "name";

    public var name:String;

    public var body:String;

    [DateTime]
    public var sent:Date;

    public var publish:Boolean;

    [BelongsTo]
    public var post:Post;

    public function Comment() {
      super(LABEL);
    }
  }
}
